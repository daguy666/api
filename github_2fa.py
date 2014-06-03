#!/usr/bin/env python
#
#github_2fa.py
#This will detect users who are in a specified
#org that have 2fa disabled
############################################

import json
import urllib2
import getpass
import sys

pw = getpass.getpass("Please enter a token: ")
org = raw_input("Org to search: ")
org_url = "https://api.github.com/orgs/%s/members?&filter=2fa_disabled&access_token=%s" % (org, pw)

try:
    request = urllib2.Request(org_url)
    result = urllib2.urlopen(request)
except urllib2.HTTPError, e:
    if e.code == 400:
        print "Bad Request"
    elif e.code == 401:
        print "Invalid Password"
    elif e.code == 404:
        print "Invalid org"
    else:
        print "Call to API failed.", e
    sys.exit(1)

twofa_json = json.load(result)

print "Users in the %s Org that do not have two factor auth enabled: " % org

for entry in twofa_json:
    print entry['login']
