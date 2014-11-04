# -*- coding: UTF-8 -*
'''
Created on 2014年11月4日

@author: RobinTang
'''


import urllib2
import time

if __name__ == "__main__":
    maxtime = 30
    mintime = 5
    timestep = 5
    waittime = mintime
    while True:
        html = ''
        try:
            html = urllib2.urlopen('http://127.0.0.1:8080/findad/').read()
            print html
        except:
            print 'server error'
        if len(html) < 5 and waittime < maxtime:
            waittime = waittime + timestep
        else:
            waittime = mintime
        print 'wait %s' % waittime
        time.sleep(waittime)
    

