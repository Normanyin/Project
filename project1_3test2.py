#!/usr/bin/python

import urllib2,urllib
import cookielib

cookiejar = cookielib.MozillaCookieJar()

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
header = { 'Referer':'http://www.canadapost.ca/cpotools/apps/track/personal/findByTrackNumber?execution=e1s1',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36',
            'Origin':'http://www.canadapost.ca'
}
class RedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_301(self, req, fp, code, msg, headers):
        print '301'
    def http_error_302(self, req, fp, code, msg, headers):
        print '302'
        url1 = fp.info()
        print url1
        #getheader("Location")
        


param={'tapByTrackSearch:trackSearch:submit_button.x':'36',
       'tapByTrackSearch:trackSearch:submit_button.y':'11',
       'tapByTrackSearch:trackSearch:trackNumbers':'LM920720377CN',
       'tapByTrackSearch:trackSearch_SUBMIT':'1',
       'javax.faces.ViewState':'v1Dxx9hSieZwMVPzZZHAPSkIfrSZM1jbO4mNTTN2U0GpxoAFjzFhwHabOEXTvMIKYyUiHf4E5tIMuqNSqP+dRYKpGsqhkV+2Tm+y5O2kdGHE2HH2c1AYdcgvvjRyYzcsTLGN8xKfqu9JfGmss6QW+w=='}
params = urllib.urlencode(param)
opener = urllib2.build_opener(RedirectHandler)

region_url = 'http://www.canadapost.ca/cpotools/apps/track/personal/findByTrackNumber?execution=e1s1'
req = urllib2.Request(url = region_url, data = params, headers = header)

#opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))

#myResponse = urllib2.urlopen(url = region_url, data = params)
#print myResponse.geturl()
fp = opener.open(req)
#print fp.code
s = fp.geturl()
#s = fp.info().getheader("Location")

print  "s = " + s
