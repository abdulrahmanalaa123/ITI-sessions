#!/bin/bash

user=$(whoami)
# the epoch timestamp in seconds
initial=1649512800
ref="$HOME/.ref_file"

if [ ! -e $ref ]
then
	touch -m $ref
fi

while :
do
	current_date=$(date +%s)
	# the second bracket is done to evaluate this as integer subtraction
	# and the other is to evaluate the value
	difference=$(($current_date - $initial))
	if [ $difference -ge 10 ]
	then
		new=`find "/var/mail" -regex ^[$user]$ -anewer "$HOME/.ref_file"`
		if [ -z $new ]
		then
			echo "no new messages"
		else
			for file in $new
			do
				cat $file
			done	
		fi	
		echo "10 seconds have passed"
		initial=$current_date
		touch -m $ref
	fi
done 
