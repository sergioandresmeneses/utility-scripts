#!/bin/bash

#Configuring the IPTables file for making the read of it easier and faster
echo "Generating the temporary IP tables file..."
iptables -L >> iptables-tmp.txt
echo "done, the number of lines in the Iptables file is: `cat iptables.txt | wc -l`"

#Read the file
#Compare the line against the IPtables file


echo "Removing the temporary IPtables file..."
rm -f iptables-temp.txt
if [ $? ]; then
	echo "Done"
else
	echo "There was an issue while removing the file, please check it out manually."
fi

