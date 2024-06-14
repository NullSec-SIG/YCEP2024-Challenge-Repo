FROM pwn.red/jail
COPY --from=ubuntu:22.04 / /srv

COPY flag /srv/app/flag
COPY chall /srv/app/run

RUN chmod +x /srv/app/run

