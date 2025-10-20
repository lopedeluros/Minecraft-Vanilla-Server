from mcrcon import MCRcon
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


import config

RCON_HOST = config.RCON_HOST
RCON_PORT = config.RCON_PORT

AUTHORIZED_USER_ID = config.AUTHORIZED_USER_ID

TELEGRAM_TOKEN = config.TELEGRAM_TOKEN
RCON_PASSWORD = config.RCON_PASSWORD

# Function to send a Minecraft command via RCON
def send_mc_command(cmd: str):
    with MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT) as mcr:
        resp = mcr.command(cmd)
        return resp

async def mc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if user_id not in AUTHORIZED_USER_ID:
        await update.message.reply_text("Unauthorized.")
        return

    if not context.args:
        await update.message.reply_text("Usage: /mc <command>")
        return

    command = " ".join(context.args)
    try:
        response = send_mc_command(command)
        if response.strip():
            await update.message.reply_text(f"✅ Server replied:\n{response}")
        else:
            await update.message.reply_text(f"✅ Command executed: {command}")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

async def wid(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Your ID is {update.effective_user.id}')

if __name__ == "__main__":

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("mc", mc))
    app.add_handler(CommandHandler("myid", wid))

    app.run_polling()
