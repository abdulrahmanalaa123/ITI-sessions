#!/bin/bash

select val in 1 2 3
do

	echo "1) ls \n 2) ls -a \n 3)exit \n"

	echo "enter a number between one and 3"
	case $val in
		1)
			ls
			;;
		2)
			ls -a	
			;;
		3)
			exit 0;
	esac
done
