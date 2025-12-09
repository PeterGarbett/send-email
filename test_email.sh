#!/bin/bash
#
# Fill out email.config with reasonable values before tryng this. 

# Use default email address in config file
#
python3 send_email.py "/etc/email.config"  "test subject" "test body" 
#
# Overide email 
#
python3 send_email.py "/etc/email.config"  "test subject" "test body" "fred@gmail.com"


