#!/bin/bash

function sq {
	if [[ $1 =~ ^[0-9]?$ ]]
	then
		result=$(($1*$1))	
		printf "\n$result\n"
		exit $result

	fi
}
echo "enter your number:"
read -n1 val
sq $val
