#!/bin/bash

echo "how large do you want your array?"

read val

typeset -i arr[$val]


for i in $(seq 1 $val)
do
	arr[$i]=$i
done


echo ${arr[@]}
