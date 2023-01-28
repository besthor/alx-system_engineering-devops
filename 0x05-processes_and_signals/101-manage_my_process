#!/usr/bin/env bash
# This script manages 'manage_my_process'

#!/usr/bin/env bash
# Manages 'manage_my_process'

if [ $# -gt 0 ]
then
    if [ "$1" == "start" ]
    then
	./manage_my_process &
	touch /var/run/my_process.pid
#	echo $(pgrep -f manage_my_process) > /var/run/my_process.pid
	echo "$!" > /var/run/my_process.pid
	echo "manage_my_process started"
    elif [ "$1" == "stop" ]
    then
#	kill $(pgrep -f manage_my_process)
	echo "manage_my_process stopped"
	kill "$(cat /var/run/my_process.pid)"
	rm -f /var/run/my_process.pid
    elif [ "$1" == "restart" ]
    then
#	kill $(pgrep -f manage_my_process)
	kill "$(cat /var/run/my_process.pid)"
	rm -f /var/run/my_process.pid
	./manage_my_process &
#	echo $(pgrep -f manage_my_process) > /var/run/my_process.pid
	touch /var/run/my_process.pid
	echo "$!" > /var/run/my_process.pid
	echo "manage_my_process restarted"
    else
	echo "Usage: manage_my_process {start|stop|restart}"
    fi
else
    echo "Usage: manage_my_process {start|stop|restart}"
fi
