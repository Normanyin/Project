#!/usr/bin/python

import urllib2,urllib
import re
import cookielib

#下面这段是关键了，将为urlib2.urlopen绑定cookies

cookiejar = cookielib.MozillaCookieJar()


# 将一个保存cookie对象，和一个HTTP的cookie的处理器绑定
cookieSupport= urllib2.HTTPCookieProcessor(cookiejar)
#下面两行为了调试的
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
#创建一个opener，将保存了cookie的http处理器，还有设置一个handler用于处理http的
opener = urllib2.build_opener(cookieSupport, httpsHandler)
#将包含了cookie、http处理器、http的handler的资源和urllib2对象绑定在一起，安装opener,此后调用urlopen()时都会使用安装过的opener对象，
urllib2.install_opener(opener)

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36'}


postdata=urllib.urlencode({'tapByTrackSearch:trackSearch:trackNumbers':'LM919103222CN',
        'tapByTrackSearch:trackSearch:submit_button.x':'37',
        'tapByTrackSearch:trackSedddarch:submit_button.y':'13',
        'autoScroll':'',
        'tapByTrackSearch:trackSearch_SUBMIT':'1',
        'javax.faces.ViewState':'v1Dxx9hSieZwMVPzZZHAPSkIfrSZM1jbO4mNTTN2U0GpxoAFjzFhwKHSEgcAunn2YyUiHf4E5tIMuqNSqP+dRYKpGsqhkV+2Tm+y5O2kdGHE2HH2c1AYdcgvvjRyYzcsTLGN8xKfqu9JfGmss6QW+w=='
        })

class RedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_301(self, req, fp, code, msg, headers):
        print '301'
    def http_error_302(self, req, fp, code, msg, headers):
        print '302'
        url1 = fp.info()
        print url1

opener = urllib2.build_opener(RedirectHandler)

req = urllib2.Request(  
    url = 'https://www.packagetrackr.com/track/canadapost/LM920934240CN?contextid=0',
#    url = 'http://www.canadapost.ca/cpotools/apps/track/personal/findByTrackNumber?execution=e1s1', 
#    data = postdata,
    headers = headers
)

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
f = opener.open(req)
s = f.read()
html =  open('html.txt','w+')
html.write(s)
html.close
#myResponse = urllib2.urlopen(req)
#print myResponse.code
#print myResponse.read()
#cur_url =  myResponse.geturl()
#print "cur_url:",cur_url

#myPage = myResponse.read()

#f = open('html.txt','a+')
#f.write(myPage)
#f.close

#print myPage
