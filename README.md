# Introduction

This project is a connection test to an Oracle database server.

## Prerequisites

You need:
* a Python 3.10 or higher
* a database [Oracle server](#oracle-docker)
* an [Oracle client installed](#install-oracle-instant-client)
* install the prerequisites.txt
* install the pre-commit hook

## Oracle docker
You can run an Oracle server using the following docker-compose.yml file.

```dockerfile
services:
  oracle-xe:
    container_name: oracle-xe
    image: container-registry.oracle.com/database/express:latest
    ports:
      - 1521:1521
    environment:
      - ORACLE_PWD=xe
    volumes:
      - db-vol-reg:/opt/oracle/oradata
    hostname: database
volumes:
  db-vol-reg:
    name: db-vol-reg
    external: false
```
To run the docker, you need to use the docker composer plugin and the command line

```bash
docker compose up -d
```

## Install Oracle instant client

To install Oracle client on Debian-based Linux systems, you can follow this
[instructions](https://github.com/ManelJimeno/Annotations/blob/main/settings/oracle.md)
