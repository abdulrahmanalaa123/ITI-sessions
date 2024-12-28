#!/bin/bash


function calc_avg {
	typeset -i sum

	sum=0
	count=0
	for elem in "$@"
	do
		sum=$(($sum + $elem))
		count=$(($count+1))
	done	
	result=$(($sum/$count))
 	
	echo $result

}
echo "enter your values"

read values

calc_avg $values
exit 

