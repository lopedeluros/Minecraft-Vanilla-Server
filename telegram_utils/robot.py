from mcrcon import MCRcon
from telegram import Update, Bot, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

from commands.cmd_parse import CmdParse
from commands.chat import Chat
import config

RCON_HOST = config.RCON_HOST
RCON_PORT = config.RCON_PORT

AUTHORIZED_USER_ID = config.AUTHORIZED_USERS

TELEGRAM_TOKEN = config.TELEGRAM_TOKEN
RCON_PASSWORD = config.RCON_PASSWORD

chat = None

# Function to send a Minecraft command via RCON
def send_mc_command(cmd: str):
    with MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT) as mcr:
        resp = mcr.command(cmd)
        return resp

    
# Execute Minecraft Server Command
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

        msg_cnf, user_msg = chat.check_mc_command(command)

        if msg_cnf:
            
            response = send_mc_command(command)
            if response.strip():
            
                msg = CmdParse.parse_command(command, response)
                
                user_rsp = f"✅ Server replied:\n{msg}"
                if user_msg != '':
                    user_rsp += f"\n{user_msg}"
            
                await update.message.reply_text(user_rsp)
            else:

                user_rsp = f"✅ Command executed: {command}"
                if user_msg != '':
                    user_rsp += f"\n{user_msg}"

                await update.message.reply_text(user_rsp)
        
        else:
            await update.message.reply_text(f"{user_msg}")
        
        
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

# Get user ID
async def wid(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Your ID is {update.effective_user.id}')


# Advanced Minecraft server commands start/reboot/stop 
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id

    if user_id not in AUTHORIZED_USER_ID:
        help_msg = chat.get_help(admin=False)
        await update.message.reply_text(help_msg)
    else:
        help_msg = chat.get_help(admin=True)
        await update.message.reply_text(help_msg)
        
    

if __name__ == "__main__":

    print("Hello World")

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Set commands
    ## Regular user
    bot = Bot(token=TELEGRAM_TOKEN) #TODO this still does not work

    commands = [
        BotCommand("myid", "Returns your user ID"),
        BotCommand("help", "Get commands available")
    ]

    bot.set_my_commands(commands=commands, scope={"type": "default"})

    # Privileged user
    advanced_commands = [
            {"command": "help", "description": "Get commands available"},
            {"command": "myid", "description": "Returns your user ID"},
            {"command": "mc", "description": "Executes server command"}          ]
    for id in AUTHORIZED_USER_ID:

        bot.set_my_commands(commands=advanced_commands,
                            scope={
                                "type": "chat_member",
                                "user_id": id
          }
        )

    chat = Chat()

    app.add_handler(CommandHandler("mc", mc))
    app.add_handler(CommandHandler("myid", wid))
    app.add_handler(CommandHandler("help", help))

    app.run_polling()
