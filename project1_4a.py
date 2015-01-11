#!/usr/bin/python

#import data from txt and get information by track number

import MySQLdb
import urllib2,urllib
import re

try:
    conn = MySQLdb.connect(host='localhost',user='root',passwd='271828')
    cur = conn.cursor()

    cur.execute('create database if not exists trackdb')
    conn.select_db('trackdb')
    cur.execute('create table track_info(id varchar(10), track_number varchar(20), date varchar(40), state varchar(40), location varchar(40))')

except MySQLdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    
def get_info():
    '''get infomation by track number'''

    lm_domain = 'https://www.packagetrackr.com/track/canadapost/'
    ln_domain = 'https://tools.usps.com/go/TrackConfirmAction?qtc_tLabels1'
    lx_domain = 'http://auspost.com.au/track/track.html'

    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }

    statline = ''
    cur.execute("select * from track_info")
    cds = cur.fetchall()

    for i in range(len(cds)):
        date_time = ''
        status = ''
        location = ''
        statline = ''
        if 'LN' in cds[i][1]:
            search_url = ln_domain + '=' +cds[i][1]
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

        elif 'LX' in cds[i][1]:
            search_url = lx_domain
            data = {'trackIds':cds[i][1]}
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
        elif 'LM' in cds[i][1]:
            search_url = lm_domain + cds[i][1].replace('\r\n','') + '?contextid=0'
            req = urllib2.Request(search_url, headers = headers)
            myResponse = urllib2.urlopen(req)
            myPage = myResponse.read()
            myItems = re.findall('track-info-showmaps"><strong>(.*?)<.*?div>.*?>(.*?)</div>.*?>(.*?)</div>',myPage, re.S)
            if myItems:
                location = myItems[0][0]
                date_time = myItems[0][1]
                status = myItems[0][2]
                statline = 'DATE/TIME:' + date_time.replace("\t","").replace("\r\n","") + ' STATUS:' + status.replace("\t","").replace("\r\n","") + ' LOCATION:' + location.replace("\t","").replace("\r\n","").replace("&nbsp;","")
        cur.execute("update track_info set date = %s, state = %s, location = %s where track_number = %s",(date_time,status,location,cds[i][1]))
        conn.commit()

def import_data(filename):
    lines = []
    i = 0
    for line in open(filename, 'r'):
        line = line.upper()
        lines.append((i,line,'','',''))
        i=i+1

    cur.executemany('insert into track_info values(%s,%s,%s,%s,%s)',lines)

    conn.commit()


if __name__ == "__main__":
    print 'The script use to import track number and get information by track number,then you want do (choose number):'

    print '0.import track number'
    print '1.get imformation by track number'
    choice = raw_input("your choice:")

    if choice == '0':
        print 'start to import track number...'
        filename = raw_input('please input filename:')
        import_data(filename)
    elif choice =='1':
        print 'start to get infomation by track number...'
        get_info()
            

    
    cur.close()
    conn.close()
        
