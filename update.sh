#!/bin/bash
date=$(date '+%Y-%m-%d')

git add .

git commit -m "udpating with ${date}"

git push
