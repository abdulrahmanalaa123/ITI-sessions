#!/bin/bash
date=$(date '+%Y-%m-%d')

git --git-dir ~/CS/devops/ITI/.git --work-tree ~/CS/devops/ITI/ add .

git --git-dir ~/CS/devops/ITI/.git --work-tree ~/CS/devops/ITI/ commit -m "udpating with ${date}"

git --git-dir ~/CS/devops/ITI/.git --work-tree ~/CS/devops/ITI/ push
