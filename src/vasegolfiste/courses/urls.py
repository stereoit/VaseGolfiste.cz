from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic import DetailView, ListView
from models import GolfCourse


urlpatterns = patterns(
    '', 
    url(r'^$', ListView.as_view(model=GolfCourse), name='golfcourse.list'),
    url(r'^(?P<slug>[-_\w]+)/$', DetailView.as_view(model=GolfCourse), name='golfcourse.detail'),
)

