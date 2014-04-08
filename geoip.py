#!/usr/bin/env python
from pprint import pprint
import json
import urllib2

ip = raw_input("Please enter the ip address you wish to get geo info for: ")
www = "http://www.freegeoip.net/json/%s" % (ip)
request = urllib2.Request(www)
result = urllib2.urlopen(request)

my_json = json.load(result)
#fixed_json = pprint(my_json)

print "You are in the country of: "
print my_json['country_name']
print "Your area code is: "
print my_json['area_code']
print "You are near the city of: "
print my_json['city']
print "You are in the state of: "
print my_json['region_name']
print "Your zip code is: "
print my_json['zipcode']
