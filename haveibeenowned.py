#!/usr/bin/env python
from pprint import pprint
import json
import urllib2
import sys

sites = """
31 pwned websites  168,443,583  pwned accounts
152,445,165 Adobe accounts 
4,789,599   Bitcoin Security Forum Gmail Dump accounts 
4,609,615   Snapchat accounts 
1,247,574   Gawker accounts 
1,057,819   Forbes accounts 
859,777 Stratfor accounts 
855,249 Manga Traders accounts 
530,270 Battlefield Heroes accounts 
453,427 Yahoo accounts 
227,746 Cannabis.com accounts 
202,683 Win7Vista Forum accounts 
191,540 hackforums.net accounts 
158,093 Boxee accounts 
148,366 WPT Amateur Poker League accounts 
116,465 Pokemon Creed accounts 
104,097 Insanelyi accounts 
56,021  Vodafone accounts 
55,622  Spirol accounts 
45,018  Lounge Board accounts 
38,108  Pixel Federation accounts 
37,784  Muslim Directory accounts 
37,103  Sony accounts 
36,789  BigMoneyJobs accounts 
35,368  Fridae accounts 
28,641  hemmelig.com accounts 
26,596  Business Acumen Magazine accounts 
20,902  Bell accounts 
16,919  Verified accounts 
5,788   Astropid accounts 
3,200   UN Internet Governance Forum accounts 
2,239   Tesco accounts 
"""

email = raw_input("Please enter the email account you would like to check: ")  # Which email address to check

if len(email) > 0:
    print "Searching for %s" % email
else:
   sys.exit(1)

www = "https://haveibeenpwned.com/api/v2/breachedaccount/%s" % email

try:
    request = urllib2.Request(www)  # url + variable
    result = urllib2.urlopen(request)
except urllib2.HTTPError, e:

    if e.code == 404:
        print "Your email address was not on any lists."
    else:
        print "Call to api failed."
else:
    my_json = json.load(result)
    print "Your email address was found on the following lists:"
    for entry in my_json:
        print entry['Name']
