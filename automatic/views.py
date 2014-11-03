# -*- coding: UTF-8 -*
'''
Created on 2014-11-01

@author: RobinTang
'''
import json

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from doubapi import get_topic_list, get_topic, comment_topic, report_topic
from models import GroupTopic

from datamining.funs import cut
import time
from base.models import Drive
from datamining.classify.bayes import NaiveBayesClassifier

ignor = '~！@#￥%……&*（）——+-=，。、；‘【】、《》？：“｛｝| ,./;<>?:"[]{}\\~!@#$%^&*()-=_+'

urls = []
def path(patrn, *args):        
    def m(func):
        def check(request, *args):
            r = func(request, *args)
            return r
        urls.append((patrn, check) + tuple(args))
        return func
    return m


def get_topicatbs(topic):
    return [t for t in cut(topic.title + ' ' + topic.text) if not t in ignor]


@path('^newtopic/')
def new_topic(request):
    lst = get_topic_list()
    ids = set([t['id'] for t in lst])
    rids = GroupTopic.objects.filter(tid__in=ids).values_list('tid', flat=True)
    map(lambda tid:ids.remove(tid), rids)
    ts = []
    count = 5
    for tid in ids:
        jt = get_topic(tid)
        t = GroupTopic(tid=tid,
                       url=jt['alt'],
                       uid=jt['author']['id'],
                       gid=jt['group']['id'],
                       title=jt['title'],
                       text=jt['content'],
                       created=jt['created'],
                       type='',
                       other='',
                       )
        if len(t.text) < 10 or len(t.text) > 1000:
            # 忽略过长过过短的
            t.type = 'i'
        t.save()
        ts.append(t)
        count = count - 1
        if not count:
            break
    cxt = RequestContext(request)
    cxt['topics'] = ts
    return HttpResponse(json.dumps([t.tid for t in ts]))


@path('^training/([0-9]+)/i')
def training_which_class(request, tid):
    t = GroupTopic.objects.filter(tid=tid, other='').first()
    t.type = 'i'
    t.save()
    return HttpResponse('ignored')

@path('^training/([0-9]+)/q')
def training_ignor_class(request, tid):
    t = GroupTopic.objects.filter(tid=tid).first()
    st = time.time()
    sample = get_topicatbs(t)
    nbc = NaiveBayesClassifier(Drive())
    r = nbc.classify(sample)
    res = '%s %s' % (r, time.time() - st)
    return HttpResponse(res)

@path('^training/([0-9]+)/([a-z]+)')
def training_to_class(request, tid, cls):
    t = GroupTopic.objects.filter(tid=tid, other='').first()
    st = time.time()
    sample = get_topicatbs(t)
    nbc = NaiveBayesClassifier(Drive())
    nbc.training(sample, cls)
    t.other = 'train'
    t.type = cls
    t.save()
    res = '%s %s' % ('/'.join(sample), time.time() - st)
    return HttpResponse(res)

@path('^training/([a-z]*)')
def training(request, act=None):
    ts = GroupTopic.objects.filter()
    if act != 'list':
        ts = ts.filter(type='')
    ts = ts[0:50]
    cxt = RequestContext(request)
    cxt['topics'] = ts
    cxt['types'] = [
                    ('ok', '正常'),
                    ('ad', '广告'),
                    ('po', '色情'),
                    ('co', '求安慰'),
                    ('ml', '约贴'),
                    ('q', '测试'),
                    ('i', '忽略'),
                    ]
    return render_to_response('training.html', cxt)

@path('^findad/([0-9]*)')
def findad(request, tid=''):
    t = None
    if tid:
        t = GroupTopic.objects.filter(tid=tid, other='').first()
    else:
        t = GroupTopic.objects.filter(type='', other='').first()
    
    
    if not t:
        return new_topic(request)
    
    st = time.time()
    sample = get_topicatbs(t)
    nbc = NaiveBayesClassifier(Drive())
    r = nbc.classify(sample)
    ct = time.time() - st
    
    t.type = max(r.items(), key=lambda x:x[1])[0]
    p = r['ad'] / (r['ad'] + r['ok'])
    t.other = 'auto'
    st = time.time()
    if p > 0.60:
        # 广告
        t.other = t.other + " ad" 
        try:
            comment_topic(t.tid, '神似广告 %s' % p)
            report_topic(t.tid)
        except:
            t.other = 'failed'
    t.save()
    rt = time.time() - st
    res = {
           'title':t.title,
           'url':t.url,
           'tid':t.tid,
           'p':p,
           'type':t.type,
           'other':t.other,
           'class_time':ct,
           'report_time':rt
           }
    return HttpResponse(json.dumps(res))

# @path('.*')
# def i(request):
#     return render_to_response('index.html')







