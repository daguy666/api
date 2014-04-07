#!/usr/bin/env python
from pprint import pprint
import json
import urllib2

""" This is using the haveibeenpwned.com api to search for owned accounts. 
You are searching for email accounts on the following compromised websites
     accounts           sites
     --------           -----
    152,445,165     Adobe accounts
    4,609,615       Snapchat accounts
    1,247,574       Gawker accounts
    1,057,819       Forbes accounts
    859,777         Stratfor accounts
    530,270         Battlefield Heroes accounts
    453,427         Yahoo accounts
    158,093         Boxee accounts
    148,366         WPT Amateur Poker League accounts
    56,021          Vodafone accounts
    55,622          Spirol accounts
    38,108          Pixel Federation accounts
    37,784          Muslim Directory accounts
    37,103          Sony accounts
    28,641          hemmelig.com accounts
    20,902          Bell accounts
    3,200           UN Internet Governance Forum accounts
    2,239           Tesco accounts
"""
email = raw_input("Please enter the email account you would like to check: ") # Which email address to check
www = "https://haveibeenpwned.com/api/v2/breachedaccount/%s" % (email) 
request = urllib2.Request(www) # url + variable 
result = urllib2.urlopen(request) 

my_json = json.load(result)
fixed_json = pprint(my_json)
print fixed_json
#json_encoded = json.dumps(my_json)
#print  json_encoded
