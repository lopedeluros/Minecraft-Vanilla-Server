#!/bin/bash

option=$1

if [ "$option" == "stop" ]; then
    docker-compose down
elif [ "$option" == "start" ]; then
    docker-compose -f docker-compose.yml up -d
elif [ "$option" == "restart" ]; then
    docker-compose down
    echo "Waiting 5 seconds to relaunch..."
    sleep 5
    docker-compose -f docker-compose.yml up -d
elif [ "$option" == "status" ]; then
    container_name="minecraft-server"  
    if [ "$(docker ps --filter "name=$container_name" --format '{{.Names}}')" == "$container_name" ]; then
        echo "$container_name is running"
    else
        echo "$container_name is stopped"
    fi
else
    echo "Options are {start|stop|restart|status}"
    exit 1
fi
