# Build image
docker build -t minecraft-server .

# Deploy (commands only available with compose)

docker compose up -d

# Access terminal

docker attach mcserver

## To escape use
Ctrl+P, Ctrl+Q

### DO NOT USE CTRL + C or it will close the server

