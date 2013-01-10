from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic import DetailView, ListView
from models import GolfClub


urlpatterns = patterns(
    '', 
    url(r'^$', ListView.as_view(model=GolfClub), name='golfclub.list'),
    url(r'^(?P<slug>[-_\w]+)/$', DetailView.as_view(model=GolfClub), name='golfclub.detail'),
)

