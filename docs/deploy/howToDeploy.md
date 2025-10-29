# Minecraft server deployment

## Generate required config file and fill it up

```bash
cat <<EOF > ./config.sh
server_url=addr
server_user=linux
server_port=22
server_pwd=linux
location=your-working-dir/MinecraftVanilla
EOF
```

## Configure server-config file

### Generate template

./utils/generate-serverconf.sh

Unless you are playing in a VPN (Hamachi, ZeroTier...) you should keep whitelist=true to avoid unwanted players in your world.

## Execute deploy script

```bash
bash deploy.sh
```

# Minecraft bot deployment

## Generate environment file

```bash
cat <<EOF > ./telegram_utils/.env
TELEGRAM_TOKEN=askBotFather
RCON_PASSWORD=configuredIn:server-config/rcon.password
AUTHORIZED_USERS=1,2,3
EOF
```

## Execute deploy script

Requires config.sh to be already created

```bash
bash utils/deploy-bot.sh
```