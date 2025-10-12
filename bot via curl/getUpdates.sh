#!/usr/bin/env bash

source .env

#curl --silent https://api.telegram.org/bot$TOKEN/getUpdates | jq

curl \
  --silent \
  -X POST \
  -H "Content-Type: application/json" \
  -d @getUpdatesRequest.json \
  https://api.telegram.org/bot$TOKEN/getUpdates | jq

