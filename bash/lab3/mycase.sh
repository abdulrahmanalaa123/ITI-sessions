#!/bin/bash

echo "enter your name"
shopt -s extglob
#removing the comment will take only one character as an input
#read -n1 name
read name

case $name in
	+([0-9]))
		echo  "number"
		;;
	+([a-z]))
		echo "small"
		;;
	+([A-Z]))
		echo  "capital"
		;;
	+([a-zA-Z0-9]))
		echo "mixed"
		;;
	*)
		echo "empty"
		;;
esac
