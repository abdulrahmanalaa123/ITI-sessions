#!/bin/bash
# assuming that the input goes in wihtout any flavors or options
# $1 is file1 and $2 is file2

if [ $# -eq 2 ];then
	first_file=$1
	second_file=$2
	# check that the parent dir is readable and the target is writable as well as check if its not a dir could add a check passing an option of -r with the same condition
	if [ -f "$first_file" ] && [ -r "$(dirname $first_file)" ] && [ ! -d "$second_file" ] && [ -w "$(dirname $second_file)" ];
	then
		cp $1 $2
	else
		echo "invalid operation"
	fi
elif [ $# -gt 2 ];then
	#the target usage method is the directory first and then the files taht needs to be copied because its easier to handle the arguments

	target_dir=$1
	if [ -d "$target_dir" ] && [ -w "$target_dir" ];then
		shift
		for i;do
			if [ -r "$(dirname $i)" ] && [ -f "$i" ];then
				cp $i "$target_dir/$i"
			else
				echo "permission denied or invalid"
			fi
		done
	else
		echo "options for multi file is mydir <dir name> <f1> ..."
	fi

else
	echo `cp --help`
fi

