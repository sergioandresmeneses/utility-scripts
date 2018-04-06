#Template of the Nginx script
#packages imported
import csv
import subprocess
import re

#Function to format the urls in the proper cases
#Queries, HTML Trans and direct format supported.
def fformat(oringUrl, destinyUrl):
    #Evaluates if the line is a query : ?
    if str(oringUrl.find("?")) != "-1":
        print ("Query!!!")
        #Split the String to make up the special rule.
        OrigUrlBefore,OrigUrlAfter = oringUrl.split("?")
        print ( "Before ?: " + OrigUrlBefore)
        print ( "After ?: " + OrigUrlAfter)
        subprocess.Popen("echo \" if ( \$query_string ~ '"+OrigUrlAfter+"' ) { rewrite '^/"+OrigUrlBefore+"/?$' "+str(destinyUrl)+"? permanent; } \" >> rules-formatted.inc", shell=True)
        print("-------------Query-----------------")

    else:
        print ("FAIL Query!!!")
    #Evaluates if the line is HTML Trash : ?
    if str(oringUrl.find("%")) != "-1":
        print ("HTML Trash!!!")
        subprocess.Popen("echo \" if ( \$request_uri ~* '^/"+str(oringUrl)+"/?$' ) { rewrite . "+str(destinyUrl)+" permanent; } \" >> rules-formatted.inc", shell=True)
        print("-------------HTML-----------------")

    else:
        print ("FAIL HTML!!!")

    #Formats the rules in the default value.
    subprocess.Popen("echo \"rewrite '^/"+str(oringUrl)+"/?$' "+str(destinyUrl)+" permanent;\" >> rules-formatted.inc", shell=True)

    pass


#Body of our script
print ("Script working...")
with open ('rules.csv') as f:

    read = csv.reader(f)
    for line in read:
        #Remove the blank spaces from the urls before any process
        line[0] = line[0].strip()
        line[1] = line[1].strip()
        fformat(line[0],line[1])

#Test added only for testing porpuses.
subprocess.Popen("echo \"------ New Test -----\" >> rules-formatted.inc", shell=True)
