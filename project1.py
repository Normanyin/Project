#!/usr/bin/python


import urllib2,urllib
import re

lm_domain = 'https://www.packagetrackr.com/track/canadapost/'
ln_domain = 'https://tools.usps.com/go/TrackConfirmAction?qtc_tLabels1'
lx_domain = 'http://auspost.com.au/track/track.html'
f = open("dst.txt",'a')

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

statline = ''

for line in open("list.txt"):
    line = line.upper()
    if 'LN' in line:
        search_url = ln_domain + '=' +line
        req = urllib2.Request(search_url,headers = headers)
        myResponse = urllib2.urlopen(req)
        myPage = myResponse.read()
        myItems = re.findall('latest-detail.*?<p>(.*?)</p>.*?<p.*?>(.*?)</p>.*?<p>(.*?)</td>.*?</tr>', myPage, re.S)
        if myItems:
            date_time = myItems[0][0]
            status = myItems[0][1]
            location = myItems[0][2]
            statline = 'DATE/TIME:' + date_time.replace("\t","").replace("\r\n","") + ' STATUS:' + status.replace("\t","").replace("\r\n","") + ' LOCATION:' + location.replace("\t","").replace("\r\n","").replace("&nbsp;","")
        else:
            statline  = 'no info'

    elif 'LX' in line:
        search_url = lx_domain
        data = {'trackIds':line}
        myResponse = urllib2.urlopen(url = search_url,data = urllib.urlencode(data))
        myPage = myResponse.read()
        myItems = re.findall('trackDeliveried.*?<td.*?>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)<', myPage, re.S)
        if myItems:
            date_time = myItems[0][0]
            status = myItems[0][1]
            location = myItems[0][2]
            statline = 'DATA/TIME:' + date_time + ' STATUS:' + status + ' LOCATION:' + location
        else:
            statline = 'no info'
    elif 'LM' in line:
        search_url = lm_domain + line.replace('\r\n','') + '?contextid=0'
        req = urllib2.Request(search_url, headers = headers)
        myResponse = urllib2.urlopen(req)
        myPage = myResponse.read()
        myItems = re.findall('track-info-showmaps"><strong>(.*?)<.*?div>.*?>(.*?)</div>.*?>(.*?)</div>',myPage, re.S)
        if myItems:
            location = myItems[0][0]
            date_time = myItems[0][1]
            status = myItems[0][2]
            statline = 'DATE/TIME:' + date_time.replace("\t","").replace("\r\n","") + ' STATUS:' + status.replace("\t","").replace("\r\n","") + ' LOCATION:' + location.replace("\t","").replace("\r\n","").replace("&nbsp;","")
    result = line.replace("\r\n","") + " " + statline.replace("\r\n","")

    print result
    f.write(result)
    f.write("\r\n")
f.close


