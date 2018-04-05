#/bin/bash
IDs=`wp user list --role="subscriber" | awk '{print $4}' | grep @something.com`
echo "$IDs"
n=`echo "$IDs" | wc -l`
echo "subscribers: $n"
echo " "

for i in $IDs
do 
    wp user delete $i --reassign=no
    echo "We have removed the user with ID: $i"
done
