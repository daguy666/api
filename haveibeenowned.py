#!/usr/bin/env python
from pprint import pprint

import json
import urllib2

email = raw_input("Please enter the email account you would like to check: ")
www = "https://haveibeenpwned.com/api/v2/breachedaccount/%s" % (email)
request = urllib2.Request(www)
result = urllib2.urlopen(request)

my_json = json.load(result)
fixed_json = pprint(my_json)
