#!/usr/bin/python

import urllib2,urllib
import re

domain = 'http://auspost.com.au/track/track.html'

data = {'trackIds':'LX903842778CN'}

myResponse = urllib2.urlopen(url = domain,data = urllib.urlencode(data))
myPage = myResponse.read()

myItems = re.findall('trackDeliveried.*?<td.*?>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)<', myPage, re.S)

# need if myItems is true ir false
#for item in myItems:
date_time = myItems[0][0]
status = myItems[0][1]
location = myItems[0][2]
statline = 'date-time:' + date_time + ' status:' + status + ' location:' + location

print statline 
