#!/bin/bash

# Author: @Th3Zer0
#
# This file is released under Public Domain.
# Feel Free. Be Free. ;)

DESTINATION=/opt/apk2java

if (( EUID == 0 )); then
	chmod a+x ./uninstall.sh
	
	cp -r ./ $DESTINATION
	
	chmod -R 777 $DESTINATION
	
	if [ ! -e "/usr/bin/apk2java" ]; then
		ln -s /opt/apk2java/apk2java /usr/bin/
	fi
else
	echo "Please, run $0 as root"
	exit 1
fi

exit
