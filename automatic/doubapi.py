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
        'Authorization': 'Bearer %s' % token,
        }
http = HttpHolder(headers=headers, timeout=30)
def get_topic_list():
    url = 'https://api.douban.com/v2/group/user_topics'
    return json.loads(http.open_html(url))[u'topics']

def get_topic(tid):
    url = 'https://api.douban.com/v2/group/topic/%s/' % tid
    return json.loads(http.open_html(url))

def report_topic(tid, reason="0"):
    url = 'https://api.douban.com/v2/group/topic/%s/report' % tid
    return json.loads(http.open_html(url, data={"reason":reason}))

def comment_topic(tid, txt, pid=''):
    url = 'https://api.douban.com/v2/group/topic/%s/add_comment' % tid
    return json.loads(http.open_html(url, data={"content":txt, "comment_id":pid}))

if __name__ == '__main__':
    print comment_topic('63160261', '哈哈哈')
#     print report_topic('65201342')









