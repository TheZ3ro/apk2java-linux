#!/bin/bash

# Author: @Th3Zer0
#
# This file is released under Public Domain.
# Feel Free. Be Free. ;)

if (( EUID == 0 )); then
	
	if [ -h "/usr/bin/apk2java" ]; then
		rm -f /usr/bin/apk2java
	fi
	
	rm -rf /opt/apk2java
	
else
	echo "Please, run $0 as root"
	exit 1
fi

exit
