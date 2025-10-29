source ../config.sh

# Build image
docker build -t minecraft-bot .

# Save image locally
docker save -o minecraft-bot.tar minecraft-bot:latest

# Copy image to server
sshpass -p "${server_pwd}" scp -P "${server_port}" minecraft-bot.tar "${server_user}@${server_url}:~/${location}/"
sshpass -p "${server_pwd}" scp -P "${server_port}" mcbot.yml "${server_user}@${server_url}:~/${location}/"

# Load and run container remotely
sshpass -p "${server_pwd}" ssh -p "${server_port}" "${server_user}@${server_url}" "
  cd ~/${location}
  docker stack deploy -c mcbot.yml mcbot &&
  rm minecraft-bot.tar
"

# Clean up
rm minecraft-bot.tar