#!/bin/bash

# running this script should be sourced for it to have effect
current_dir=$(dirname $0)
# put into a function to call it later so all functions would be defined and they are defined in probable order of execution
main () {
	#if the file contains the -s flag use the default settings
	if [[ "${@//-/}" =  s ]]
	then
		check_dir "default_env"
		setup
		return 0
	else
		echo -e "please enter your env name: "
		read env_name 
		check_dir $env_name
		setup
	fi


	select opt in "load" "freeze" "interactive" "return"
	do
		case $REPLY in
			1)
				load
				;;
			2)
				freeze
				;;
			3)
				prepping
				return 0
				;;
			4)
				echo ""
				return 0
				;;
			*)
				echo "please enter a valid option"
				;;
		esac	
	done
}

setup () {
	# using -m runs the venv module found in the sysfile form python
	python3 -m venv "$path"
	# activating the current venv as your main python env
	source "$path/bin/activate"
}

check_dir () {

	path="$current_dir/$1"
	echo "$path"
	if [[ -d $path ]]
	then
		echo "already exists"
		return 1
	fi
}


freeze () {

	echo "enter your requirements file"
	read req
	
	pip freeze >> "$current_dir/$req"
}

load () {
	
	echo  "please specify your requirements file location and name: "	
	read req
	pip install -r $req	
}

prepping () {

	select opt in "install a library" "freeze" "quit" 
	do
		case $REPLY in
			1)
				echo "enter library name: "
				read lib
				pip install $lib
				;;
			2)
				freeze
				;;
			3)
				break
				;;
			*)
				echo "please enter a valid option"
				;;
		esac	
	done
}


main $@
