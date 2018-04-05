#/bin/bash

#We get a list of all the users with roll "subscriber" and filter them by the domain of the email.
IDs=`wp user list --role="subscriber" | awk '{print $4}' | grep @something.com`

#Print the total number of the users we found.
n=`echo "$IDs" | wc -l`
echo "subscribers: $n"
echo " "

#Run a 'FOR' for removing them.
for i in $IDs
do 
    wp user delete $i --reassign=no
    echo "We have removed the user with ID: $i"
done
