#!/bin/bash
typeset -i arr[1200]


for i in $(seq 1 1200)
do
	arr[$i]=$i
done

#for ele in ${!arr[@]}
#do
#	echo "index is $ele"	
#done

echo ${arr[@]}
