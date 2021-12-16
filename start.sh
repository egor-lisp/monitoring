#!/bin/bash
until main.py; do
    echo "'main.py' exited with code $?. Restarting..." >&2
    sleep 1
done
