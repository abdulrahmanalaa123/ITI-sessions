#!/bin/bash

users=`grep /bin/bash /etc/passwd | cut -d: -f1`

for user in $users
do
	echo $user
	mail -f "$(pwd)/bla.txt" "$user@tomail.org" 
done
