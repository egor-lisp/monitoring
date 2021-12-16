#!/bin/bash
until maint.py; do
    echo "'main.py' exited with code $?. Restarting..." >&2
    sleep 1
done