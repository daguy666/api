#!/usr/bin/env python
#Offline geo ip lookup
#You are going to need to install pygeoip
#pip install pygeoip
################################

import pygeoip
import sys

geodb = '/usr/local/geo/GeoLiteCity.dat'
try:
  gic = pygeoip.GeoIP(geodb)
except IOError:
  print "Cannot open %s." % geodb
  sys.exit(1)
  
ip = raw_input('Please enter the ip you want to look up: ')
try:
  gic.record_by_addr(ip)
except:
  print "Could not look up IP: %s" % ip
  sys.exit(1)
  
my_json = gic.record_by_addr(ip)

print "The Geoinfo for %s is: " % ip
print 'City: %s Region: %s County: %s' % (my_json['city'], my_json['region_code'], my_json['country_code'])
