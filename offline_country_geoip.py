#!/usr/bin/env python
# Offline geoip lookup 

import pygeoip

gi = pygeoip.GeoIP('/usr/local/geo/GeoIP.dat')
url = raw_input("Wich url would you like to locate: ")
print gi.country_code_by_name(url)
