#!/usr/bin/env python
import urllib2
import json

tiny = raw_input("Enter short URL: ")
url = "http://api.longurl.org/v2/expand?format=json&url=%s" % tiny

try:
    request = urllib2.Request(url)
    result = urllib2.urlopen(request)
except urllib2.HTTPError, e:

    if e.code == 400:
        print "Bad Request"
    if e.code == 404:
        print "Not Found"
    else:
        print "Call to API failed"

long_json = json.load(result)

print(long_json)
