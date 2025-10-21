#!/bin/bash
set -e

echo "Initiating deployment. Warning: this script assumes previous steps are completed."
source ./config.sh

# Build image
docker build -t minecraft-server .

# Save image locally
docker save -o minecraft-server.tar minecraft-server:latest


# Will require password to install packages
sshpass -p "${server_pwd}" ssh -t -p "${server_port}" "${server_user}@${server_url}" "
  mkdir -p ~/${location} &&
  cd ~/${location} &&
  sudo apt update &&
  sudo apt install -y docker.io sshpass net-tools docker-compose &&
  sudo usermod -aG docker ${server_user}
"

sshpass -p "${server_pwd}" ssh -t -p "${server_port}" "${server_user}@${server_url}" "
  docker swarm init || true
  docker network create -d overlay --attachable minecraft-net || true
"

# Copy image to server
sshpass -p "${server_pwd}" scp -P "${server_port}" minecraft-server.tar "${server_user}@${server_url}:~/${location}/"
sshpass -p "${server_pwd}" scp -P "${server_port}" docker-compose.yml "${server_user}@${server_url}:~/${location}/"
sshpass -p "${server_pwd}" scp -P "${server_port}" server-config.txt "${server_user}@${server_url}:~/${location}/"
sshpass -p "${server_pwd}" scp -P "${server_port}" utils/server.sh "${server_user}@${server_url}:~/${location}/"


# Load and run container remotely
sshpass -p "${server_pwd}" ssh -p "${server_port}" "${server_user}@${server_url}" "
  cd ~/${location}
  docker load -i ~/${location}/minecraft-server.tar &&
  if [ \$(docker ps --filter 'name=minecraft-server' --format '{{.Names}}') == 'minecraft-server' ]; then
      echo 'Server is already running! Deployment aborted to prevent disaster.' &&
      exit 1
  else
    docker-compose -f docker-compose.yml up -d
  fi
  rm minecraft-server.tar
"

# Clean up
rm minecraft-server.tar