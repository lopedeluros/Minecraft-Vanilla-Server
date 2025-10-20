# About this repository.

This repository allows an user to launch a Minecraft server using Docker through Docker compose.

The repository optionally allows to launch a Telegram Bot to send commands through it. This bot is meant to be launched through docker swarm and shares the same network as the server.

## Current configuration

- Minecraft-Vanilla version 1.21.8
- Python 3.12.3. For library info, consult [requirements](telegram_utils/requirements.txt)

# Steps to deploy on local

## Configure server

```bash
./utils/generate-serverconf.sh 
```

## Build image

```bash
docker build -t minecraft-server .
```

## Deploy (commands only available with compose)

```bash
docker compose up -d
```

## Access the server's GUI to launch commands

```bash
docker attach mcserver
```

### To escape use
Ctrl+P, Ctrl+Q

CAUTION. DO NOT USE CTRL + C or it will end the process with the server.

### Accesing the server

In your

## Optional. Launch bot

In [telegram_utils](telegram_utils/.) create a file named .env with the following content:

```bash
cat <<EOF > ./telegram_utils/.env
TELEGRAM_TOKEN=askBotFather
RCON_PASSWORD=configuredIn:server-config/rcon.password
AUTHORIZED_USERS=1,2,3
EOF
```

