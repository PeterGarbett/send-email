Email sender...

I use this to notify myself ... 

Encapsulate the gubbins required to send email using a google account.
Hide the details I don't want public in a json config file. The
config file is in the format

[ "email account" , "password" , "default destination email"]

Which needs to be filled out with correct data before use.

# Use default email address in config file
#
python3 send_email.py "./email.config"  "test subject" "test body" 
#
# Overide email 
#
python3 send_email.py "./email.config"  "test subject" "test body" "petegarbett1958@gmail.com"


