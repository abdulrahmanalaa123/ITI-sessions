#!/bin/bash

read -p "your login name please :" name


ls -rla "/home/$name"
cp -r "/home/$name" "/tmp"& 
ps -u $name
