#!/bin/bash

regex="^-[l|i|R|a|d]" 

flag=0
concat_str=""

if [ $# -ge 1 ];then
	for i;do
		echo $i
		if [[ $i =~ $regex ]];then
			concat_str="$concat_str $i"
			shift
		else

			if [ -d $i ];then
				flag=1
				path="$concat_str $i"
				ls $path
			else
				echo "invalid arguemtns"
			fi
		fi
	done
	if [ $flag -eq 0 ];then
		path="$concat_str $(pwd)"
		ls $path
	fi
else
	ls $(pwd)
fi
