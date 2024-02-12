## Introduction

This repository contains studies for kafka....

## Installation

We are using docker compose to install kafka locally. We are following the tutorial provided here: https://docs.confluent.io/platform/current/platform-quickstart.html

```bash

# start docker compose in the same directory containing docker-compose.yml file.
1. docker-compose up

# after docker compose is running, we can run some commands
# create a topic called wikimedia
2. docker-compose exec broker kafka-topics --create --topic wikimedia --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092

# list existing topics
3. docker-compose exec broker kafka-topics --list --bootstrap-server localhost:9092

# consume topic messages
4. docker-compose exec broker kafka-console-consumer --topic wikimedia --from-beginning --bootstrap-server localhost:9092

# stop docker-compose
5. docker-compose stop
```