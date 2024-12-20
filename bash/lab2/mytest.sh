#!/bin/bash

if [ $# -ge 1 ];then
	if [ -f $1 ];then
		echo "file"
	elif [ -d $1 ];then
		echo "directory"
	fi
	if [ -r $1 ];then
		echo "readable"
	fi
	if [ -w $1 ];then
		echo "writeable"
	fi
	if [ -x $1 ];then
		echo "executable"
	fi
else
	echo "please enter a file or directory as an argument"
fi
