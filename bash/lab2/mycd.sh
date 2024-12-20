#!/bin/bash

#run with source to affect the shell you're currently running
# you could create an alias writing the alias mycd="source <location/mycd>"
if [ $# -ge 1 ];then
	if [ -d $1 ];then
		 cd $1
	else
		echo "directory doesnt exist"
		exit 1
	fi
else
	 cd ~
fi
