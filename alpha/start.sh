#!/usr/bin

echo "start processing..."

sudo docker container stop rabbitmq &> /dev/null
if [[ ! "$?" ]]; then
    sudo docker container rm rabbitmq
fi
echo "rm docker rabbitmq done."

sudo docker container stop redis &> /dev/null
if [[ ! "$?" ]]; then
  sudo docker container rm redis
fi
echo "rm docker redis done."
