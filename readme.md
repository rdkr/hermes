# hermes

a system to find common availability times across multiple users

it consists of:

- python discord bot (kubernetes)
- react spa ui (s3)
- go backend (kubernetes)
- postgres db (kubernetes)
- grpc between components

this code is mostly not production quality and is written to experiement with various technologies

## proto

contains protobuf definitions and makefile to generate code in the frontend / gateway

## scheduler

contains the python discord bot and database schema versioning with sqlachemy and alembic

## database

contains kubernetes resources to deploy postgres

## gateway

go app with envoy grpc gateway which connects to db

## frontend

react spa which connects to the gateway