FROM ubuntu:22.04

RUN apt-get update && apt-get install -y socat

RUN useradd -m ycepuser

RUN mkdir -p /home/ycepuser/flag_in_here

COPY /shell.sh /shell.sh
COPY flag /home/ycepuser/flag_in_here/.flag
COPY README /home/ycepuser/flag_in_here/README

RUN chmod +x /shell.sh

USER ycepuser

WORKDIR /home/ycepuser

EXPOSE 13337

CMD ["socat", "-T60", "TCP-LISTEN:13337,reuseaddr,fork", "EXEC:/shell.sh"]

