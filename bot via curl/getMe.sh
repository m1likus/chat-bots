#!/usr/bin/env bash

source .env

curl --silent https://api.telegram.org/bot$TOKEN/getMe | jq