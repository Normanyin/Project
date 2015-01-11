# -*- coding: utf-8 -*-
#---------------------------------------
#   程序：智联招聘爬虫
#   版本：0.2
#   作者：andrew9tech
#   日期：2014-12-24
#   语言：Python 2.7
#   操作：
#   功能：
#---------------------------------------

import urllib  
import urllib2
import cookielib
import AddCookieHandler
import Cookie



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


#下载验证码图片，手动输入
f = open('img.gif', 'wb')
stream = urllib2.urlopen('http://rd2.zhaopin.com/s/loginmgr/picturetimestamp.asp').read()
f.write(stream)
f.close()

#手动输入验证码
text = raw_input('input yan zheng ma:：')
print len(text)


#需要POST的数据#
postdata=urllib.urlencode({  
    'username':'feiba_xinxin',  
    'password':'63de29486',
    'Validate':text,
    'Submit':''
})

#伪装成浏览器，加入headers
headers = {
    'Content-Type':'application/x-www-form-urlencoded',
    'Origin':'http://rd2.zhaopin.com',
    'Referer':'http://rd2.zhaopin.com/portal/myrd/regnew.asp?za=2',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36'    
    
    }


#自定义一个请求
req = urllib2.Request(  
    url = 'http://rd2.zhaopin.com/loginmgr/loginproc.asp?DYWE=Date.parse(new%20Date())', 
    data = postdata,
    headers = headers
)

#访问该链接#
response = urllib2.urlopen(req)

#打印响应信息
info = response.info()
print info
#输出当前url
cur_url =  response.geturl()
print "cur_url:",cur_url
status = response.getcode()
print status


FinalPage = urllib2.urlopen(cur_url)
#PrintOut = FinalPage.read().decode('GBK')
#print PrintOut

#简历搜索页面
SearchUrl = 'http://rdsearch.zhaopin.com'
response = opener.open(SearchUrl)
#PrintOut = FinalPage.read().decode('utf-8')
#print PrintOut
#打印当前cookies
print type(cookiejar)
for ck in cookiejar:
    print type(ck)
    print ck.name,':',ck.value





#验证有木有成功
SearchUrl2 = 'http://rdsearch.zhaopin.com/Home/ResultForCustom?SF_1_1_11=%E5%8D%8E%E4%B8%AD%E7%A7%91%E6%8A%80%E5%A4%A7%E5%AD%A6&SF_1_1_5=7%2C16&orderBy=DATE_MODIFIED,1&SF_1_1_27=0&exclude=1'
headers2 = {
    #'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    #-------------------------------------
    #此句误加，否则网络以gzip格式传输，无法解码
    #'Accept-Encoding':'gzip,deflate,sdch',
    #--------------------------------------
    #'Accept-Language':'zh-CN,zh;q=0.8',
    #'Cache-Control':'max-age=0',
    #'Connection':'keep-alive',
    #'Host':'rdsearch.zhaopin.com',
    'Referer':'http://rdsearch.zhaopin.com/',
    #'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36'    
    }

#自定义一个请求2
req2 = urllib2.Request(  
    url = SearchUrl2, 
    headers = headers2
)

FinalPage2 = urllib2.urlopen(req2)
PrintOut2 = FinalPage2.read().decode('utf-8')
print PrintOut2
cur_url =  FinalPage2.geturl()
print "cur_url:",cur_url
