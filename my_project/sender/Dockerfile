FROM debian:stretch

WORKDIR ./sender

RUN apt-get update > /dev/null &&  apt-get -y -q install \
    python3-pip > /dev/null

RUN pip3 install pika pyyaml

COPY . sender/

CMD ["/usr/bin/python3", "/sender/sender.py"]
