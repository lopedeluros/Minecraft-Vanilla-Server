# About this repository.

This repository allows an user to launch a Minecraft server using Docker through Docker compose. The server is intended for playing with friends, not for a big deployment.

The repository optionally allows to launch a Telegram Bot to send commands through it. This bot is meant to be launched through docker swarm and shares the same network as the server. This functionality will allow you and your friends to control it externally without needing advanced knowledge of docker. 

Why not just give op to everyone?
Giving everyone OP would be the simplest solution. However, in my experience, having OP available in-game can be tempting leading to commands like

```bash
set time day
tp me myfriend
gamemode creative
```

Which may disrupt the intended gameplay experience. As probably users will be tempted to use op privileges whenever something has gone wrong:
- An accidental fall or mob ambush leading to a respawn -> 'No worries I'll just tp to you guys'
- Building is so boring, I dont wanna gather stuff -> 'I'll just create it in creative mode'


## Current configuration

- Minecraft-Vanilla version 1.21.10
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

CAUTION. DO NOT rebuild the image on production server as it may lead to a version update which can corrupt your worlds.

## Deploy (commands only available with compose)

```bash
docker compose up -d
```

## Access the server's GUI to launch commands

```bash
docker attach minecraft-server
```

### To escape use
Ctrl+P, Ctrl+Q

CAUTION. DO NOT USE CTRL + C or it will end the process with the server.

### Accesing the server

In your

## Optional. Launch bot

The bot currently listens for messages from users whose Telegram IDs are listed in the AUTHORIZED_USERS variable inside the [.env](telegram_utils/.env) file.

Authorized users can send Minecraft server commands to the bot, which will execute them directly on the server.
Additionally, if you don’t know your own Telegram ID, you can simply message the bot — it will reply with your ID.

Current commands are:
- /mc <minecraft-command>. This is used to send a command to the bot, it will redirect it to the server.
- /myid. Use it to ask the bot for the ID you need to use to enable its service. 

To set up the environment, create the .env file inside the telegram_utils

```bash
cat <<EOF > ./telegram_utils/.env
TELEGRAM_TOKEN=askBotFather
RCON_PASSWORD=configuredIn:server-config/rcon.password
AUTHORIZED_USERS=1,2,3
EOF
```

The [file](telegram_utils/.env) must be correctly configured in order to proceed

### Launch bot as docker swarm

Init swarm if not done

```bash
docker swarm init
```

#### Create network

```bash
docker network create -d overlay --attachable minecraft-net
```

#### Launch bot process

```bash
docker stack deploy -c telegram_utils/mcbot.yml mcbot
```

#### Remove bot process

```bash
docker stack rm mcbot
```

# Automatic deployment


## Generate required config file a fill it up

```bash
cat <<EOF > ./telegram_utils/.env
server_url=addr
server_user=linux
server_port=22
server_pwd=linux
location=your-working-dir/MinecraftVanilla
EOF
```

## Execute deploy script

```bash
bash deploy.sh
```


