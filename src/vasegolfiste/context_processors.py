from django.conf import settings
from django.contrib.sites.models import Site


def common_data(request):
    return {
        'site': Site.objects.get_current(),
        'DEBUG': settings.DEBUG,
        'STATIC_MEDIA_VERSION': settings.STATIC_MEDIA_VERSION,
    }

