FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
  xinetd python3 \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /challenge
RUN useradd -M -d /challenge ctf
WORKDIR /challenge

COPY ctf.xinetd /etc/xinetd.d/ctf
COPY . /challenge/

RUN chown -R ctf:ctf /challenge && chmod -R 770 /challenge
RUN chown -R root:ctf /challenge && \
  chmod -R 750 /challenge

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

CMD ["/usr/sbin/xinetd", "-dontfork"]

EXPOSE 1337