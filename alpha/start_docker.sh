#!/usr/bin/env bash

echo "start docker ..."

sudo docker container stop rabbitmq 2> /dev/null
if [[ ! "$?" ]]; then
    sudo docker container rm rabbitmq
fi
echo "rm docker rabbitmq done."

sudo docker container stop redis 2> /dev/null
if [[ ! "$?" ]]; then
  sudo docker container rm redis
fi
echo "rm docker redis done."

sudo docker container prune

sudo docker run -it -d --name rabbitmq  \
  -p 5672:5672 \
  -p 5671:5671 \
  -p 4369:4369 \
  -p  25672:25672 \
  rabbitmq
echo "succeed to start docker rabbitmq"

sudo docker run -it -d --name redis -p 6379:6379 redis
echo "succeed to start docker redis"
