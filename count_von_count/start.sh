#!/bin/bash
echo "Starting up"
python kafka_counter.py

# Infinite Sleep: to stop the container from dying on code errors
while true; do echo 'sleeping'; sleep 10000; done
