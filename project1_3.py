#!/usr/bin/python

import urllib2,urllib
import re
import PyV8

domain = 'http://www.17track.net/zh-cn/external-call.shtml'

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent,
            'Referer':'http://www.17track.net/zh-cn/external-call.shtml'}


url1 = 'http://www.17track.net/api/zh-cn/result/post.shtml?lo=www.17track.net&num=LM922500524CN&et=0&theme=default&r=0.7138365293304639'

ctxt = PyV8.JSContext()        
ctxt.enter()               
func = ctxt.eval('''
function yqtrack(e,t,n,r,i,s,o,u){o==="cn"?o="zh-CN":o==="hk"&&(o="zh-HK"),yqtrack_v4({container:e,width:t,height:n,num:s,et:r,cc:i,lng:o,theme:u})}function yqtrack_v4(e){var t=e.container,n=isNaN(e.width)||e.width<600?600:e.width,r=isNaN(e.height)||e.w<400?400:e.height,i=e.num,s=isNaN(e.et)?0:e.et,o=isNaN(e.pt)?0:e.pt,u=isNaN(e.cm)?0:e.cm,a=isNaN(e.cc)?0:e.cc,f=e.lng?e.lng:"en",l=e.theme?e.theme:"default";if(t.hasChildNodes())while(t.childNodes.length>0)t.removeChild(t.childNodes[t.childNodes.length-1]);f||(f="en"),s=parseInt(s,10),s=isNaN(s)?0:s,o=parseInt(o,10),u=parseInt(u,10),a=parseInt(a,10),i=i.toUpperCase();var c=document.location.host,h=document.createElement("iframe");h.setAttribute("scrolling","no"),h.setAttribute("width",n),h.setAttribute("height",r);var p="//www.17track.net/api/"+f+"/result/"+(s===0?"post":"express")+".shtml?"+"lo="+c+"&num="+i+"&et="+s;s===0&&o&&(p+="&pt="+o),s===0&&u&&(p+="&cm="+u),s===0&&a&&(p+="&cc="+a),p+="&theme="+l+"&r="+Math.random(),t.appendChild(h),h.setAttribute("src",p)};
    function doTrack() {
        var num = 'LM922500524CN';
        yqtrack_v4({
            container: document.getElementById('track_container'),
            width: 800,
            height: 600,
            num: num,
            et: document.getElementById('yq_et').value,
            lng: 'zh-CN'
        });
    }
     
<input name="" maxlength="38" type="text" id="yq_num" value=""/>
<input type="button" value="TRACK" onclick="doTrack()"/>
<div id="track_container"></div>
''')

print func()


    


#data = {'tapByTrackSearch:trackSearch:trackNumbers':'LM919103222CN','tapByTrackSearch:trackSearch:submit_button.x':'37','tapByTrackSearch:trackSearch:submit_button.y':'13','autoScroll':'','tapByTrackSearch:trackSearch_SUBMIT':'1','javax.faces.ViewState':'v1Dxx9hSieZwMVPzZZHAPSkIfrSZM1jbO4mNTTN2U0GpxoAFjzFhwD6g7g7t6yKWYyUiHf4E5tIMuqNSqP+dRYKpGsqhkV+2Tm+y5O2kdGHE2HH2c1AYdcgvvjRyYzcsTLGN8xKfqu9JfGmss6QW+w=='}

#req = urllib2.Request(url = url1)
#myResponse = urllib2.urlopen(url1)
#myPage = myResponse.read()

#print myPage
    
