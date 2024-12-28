#!/bin/bash

dir=$(pwd)

for file in "$dir"/*
do
	chmod u+x $file
	echo "made $file executable"
done
