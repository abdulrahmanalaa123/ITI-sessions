#!/bin/bash

echo keep in mind typing sudo will go to the sudo home dir
echo where do you want your dir?
read dir

if [  -d $dir ]
then
	tar -cf "$dir/backup.tar" $HOME
else
	mkdir $dir
	tar -cf "$dir/backup.tar" $HOME 
fi
