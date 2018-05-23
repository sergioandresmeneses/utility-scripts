# utility-scripts

 = Requisites =

 - Python 3+
 - Bash
 - WordPres CLI

- - - - - - - - - - - - - - -
 = File Structure =

 ../Nginx/converter-rules.py

This script is a mix with Python&Bash and it's goal is to convert different formats of redirect rules into Nginx format: .inc


 ../WordPress/remove-user.sh

This script is a mix with Bash&WPcli to remove all the users in a WP site based on a certain role and being part of a email domain.

It can be adjusted to remove only for role or email.

 ../WordPress/check-IP.sh
 
 This script will validate the given address or list of addresses are blocked by our system.


*Note: *

If you are using a Mac system, please have in mind to remove the DS files before any action on the repository:
https://stackoverflow.com/questions/107701/how-can-i-remove-ds-store-files-from-a-git-repository
