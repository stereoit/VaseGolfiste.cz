from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic.base import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vasegolfiste.views.home', name='home'),
     url(r'^kluby/', include('vasegolfiste.clubs.urls')),
     url(r'^hriste/', include('vasegolfiste.courses.urls')),
     url(r'^novinky/', include('news.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #('^narrow/$', TemplateView.as_view(template_name='index-narrow.html')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    ('^$', TemplateView.as_view(template_name='index.html'))
)

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT,
        }),
    )

