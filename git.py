#!/usr/bin/env python
#
#Downloads user list for organization
#################################

from pprint import pprint
from github3 import login
import json
import urllib2

org = raw_input("Please enter orginization you want to search: ") # org you want to search
pw = raw_input("Please enter gitup authentication key: ") # auth key
www = "https://api.github.com/orgs/%s/members?access_token=%s&per_page=1000"  % (org,pw) #url pw and org 

try:
    request = urllib2.Request(www) # url
    result = urllib2.urlopen(request)
except urllib2.HTTPError, e:

    if e.code == 404:
        print "IP Address or Page not found."
    else:
        print "Call to api failed."
else:
    my_json = json.load(result)
#fixed_json = pprint(my_json)

    for entry in my_json:
        print ""
        print entry['login']
        print entry['url']
