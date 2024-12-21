#!/bin/bash
typeset -i v
v=0

for i;
do
	echo "did it once"
	echo "i's value is $v"
	echo $i;
	shift;
	v=$v+1
done

