# Dockerization

The solution to this challenge is intended to be
rather trivial. The goal of this challenge is to
encourage participants to download and learn how
to use Docker to spin up local challenges.

## Solution

Participants are required to install Docker onto
their machines and bring the challenge up with
`docker compose up`. They should then visit
`http://localhost:6969` to view the flag.

---

## Pitfalls

There might be some pitfalls that prevents the
participants from completing this challenge. This
section provides a rough guideline on how to resolve
possible issues.

### 1. Slow Wifi Speeds

The NPWirelessx wifi might get cockblocked due to the
large number of traffic flowing through. As Docker is
a rather large program, we can do the following:

1. Attempt other challenges while Docker downloads
2. Use a personal hotspot to achieve higher download
speeds. (Not recommended as Docker is fucking massive)

### 2. Incompatible device with Docker

Participants may not be running a proper laptop
that can install Docker, such as Chromebooks and iPads.
To fix:

1. Question them on their choice of device and encourage
them to change it if they want to play future CTFs.
2. Ask them to find another teammate that has a device
that supports Docker and solve the challenge there.
