FROM debian:stretch

WORKDIR ./reciever

RUN apt-get update > /dev/null &&  apt-get -y -q install \
    python3-pip > /dev/null
RUN pip3 install pika pyyaml
RUN mkdir /var/log/receiver

COPY . reciever/

CMD ["/usr/bin/python3", "reciever/"]
