#!/usr/bin/python

#encoding:utf-8
import urllib2,re,urllib,sys
import time,csv,json
import httplib

user_agent = 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)'
header = {'User-Agent':user_agent}
baseUrl='vip.com'
gCookie=''

class HTTPCookieRedirectHandler(urllib2.HTTPRedirectHandler):
    __cookie_flag='Set-Cookie: '
    @staticmethod
    def __find_cookie(headers):
        global gCookie
        if gCookie != '':
            return
        
        print 'Headers is ',headers
        res=''
        for msg in headers:
            if msg.find(HTTPCookieRedirectHandler.__cookie_flag)!=-1:
                print msg
                temp = msg.replace(HTTPCookieRedirectHandler.__cookie_flag,'')
                temp = temp.strip()+';'
                res = res + temp
        print 'res is ',res
        gCookie = res
        return res

    def http_error_301(self,req,fp,code,msg,httpmsg):
        cookie = HTTPCookieRedirectHandler.__find_cookie(httpmsg.headers)
        if cookie != '':
            req.add_header("Cookie",cookie)
        return urllib2.HTTPRedirectHandler.http_error_301(self, req, fp, code, msg, httpmsg)

    def http_error_302(self,req,fp,code,msg,httpmsg):
        HTTPCookieRedirectHandler.__find_cookie(httpmsg.headers)
        if gCookie != '':
            req.add_header("Cookie",gCookie)
        print 'Location is ',fp.info().getheader("Location"),fp.code
        return urllib2.HTTPRedirectHandler.http_error_302(self, req, fp, code, msg, httpmsg)
    
#*********************************************************
#The main function
#********************************************************* 
if __name__ == "__main__":
    print 'Start catching......'
    param={'tapByTrackSearch:trackSearch:submit_button.x':36,'tapByTrackSearch:trackSearch:submit_button.y':11,\
           'tapByTrackSearch:trackSearch:trackNumbers':'LM920720377CN','tapByTrackSearch:trackSearch_SUBMIT':1}
    params = urllib.urlencode(param)
    print params  
    httplib.HTTPConnection.debuglevel = 1
    opener = urllib2.build_opener(HTTPCookieRedirectHandler())
    
    region3URL='http://www.canadapost.ca/cpotools/apps/track/personal/findByTrackNumber?execution=e1s1'
    req = urllib2.Request(url=region3URL,data=params,headers=header)
    fp = opener.open(req)
    print fp.code, fp.url

    print 'Done!'
