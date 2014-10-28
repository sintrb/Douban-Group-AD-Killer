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

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DGADK.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^t/([a-zA-Z0-9]+)', tdm),
)
