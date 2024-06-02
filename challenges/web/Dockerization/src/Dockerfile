# Docker executes the code in this file on a normal Linux machine
# just like how a human would type commands in.

# Refer to: https://docs.docker.com/language/python/containerize/ to learn more
# (I sorta copied this file from the link above)

# If u wanna learn more try the following search terms:
# Docker, Docker containers, Dockerfile

# These fireship videos are kinda ice cold:
# * https://youtu.be/Gjnup-PuquQ
# * https://youtu.be/rIrNIzy6U_g

FROM python:3.12-slim as base

# Environment variables to tell Python to shut up
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Sets the working directory to /app
WORKDIR /app

# Creates a less privileged user (Good practice)
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "10001" \
    ycepuser

# This is some cache stuff, main thing here is:
# pip install -r requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python3 -m pip install -r requirements.txt

# Change to the newly created user
USER ycepuser

# Copy the challenge files into the Docker container
COPY . .

# Needed to run the damn .so file
ENV LD_LIBRARY_PATH="/app"

# Exposes the port the app is running on
# Defined at main.py line 22
EXPOSE 6969

# Actually runs the app 😱
CMD python3 main.py
