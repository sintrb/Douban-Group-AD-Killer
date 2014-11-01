# -*- coding: UTF-8 -*
'''
Created on 2014年11月1日

@author: RobinTang
'''

from third.HttpHolder import HttpHolder
import json
token = '???'

headers = {
        # Chrome User-Agent
        'User-Agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36',
        'Authorization': 'Bearer 7bb945a63752b9be732bd0f2a5f82d3a',
        }
http = HttpHolder(headers=headers, timeout=30)
def get_topic_list():
    url = 'https://api.douban.com/v2/group/user_topics'
    return json.loads(http.open_html(url))[u'topics']

def get_topic(tid):
    url = 'https://api.douban.com/v2/group/topic/%s/'%tid
    return json.loads(http.open_html(url))

if __name__ == '__main__':
    print get_topic_list()









