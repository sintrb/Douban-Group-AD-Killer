from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from datamining.classify.bayes import NaiveBayesClassifier, test_classifer
from base.models import Drive
from django.http import HttpResponse
import time
def tdm(request, txt):
    st = time.time()
    nbc = NaiveBayesClassifier(Drive())
#     test_classifer(nbc)
    c = nbc.whichclass(txt)
    return HttpResponse('%ss  %s'%(time.time()-st, c))


from automatic import views as automaticviews

newurl = []
newurl.extend([url(*arg) for arg in automaticviews.urls])
newurl.append(url(r'^admin/', include(admin.site.urls)))
urlpatterns = patterns('', *newurl)


