#!/usr/bin/python

import MySQLdb

try:
    conn = MySQLdb.connect(host='localhost',user='root',passwd='271828')
    cur = conn.cursor()

    #cur.execute('create database if not exists python')
    conn.select_db('python')
    #cur.execute('create table test(id int, info varchar(20))')

    value = [1, 'hi rollen']

    #cur.execute('insert into test value(%s,%s)',value)

    values=[]

    for i in range(20):
        values.append((i,'hi rollen'+str(i)))

    #cur.executemany('insert into test values(%s,%s)',values)
    #cur.execute('update test set info = "I am rollen" where id = 3')

    cur.execute("select * from test")
    cds = cur.fetchall()


    for i in range(len(cds)):
        print cds[i][1]


    conn.commit()
    cur.close()
    conn.close()

except MySQLdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
