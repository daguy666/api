#!/usr/bin/env python
#Offline geoip city lookup

import pygeoip

gic = pygeoip.GeoIP('/usr/local/geo/GeoLiteCity.dat')
ip = raw_input('Which ip would you like to locate: ')
gic.record_by_addr(ip)


my_json = gic.record_by_addr(ip)


print "The results for %sis as follows:" % ip
print my_json['city']
print my_json['country_code']
print my_json['country_name']
print my_json['metro_code']
print my_json['postal_code']
print my_json['region_code']