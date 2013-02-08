import re
from django.conf import settings
from django import template
register = template.Library()


def convert(coordinates):
    '''Convert position to decimal '''
    coor_regex = r"(.*),(.*)"
    pos_regex = r"\s*(\d+)\D*(\d+)\D*([\d.]+)\D*([WESN])\D*"
    m = re.match(coor_regex, coordinates)
    lat_lon = []
    positions = m.groups()
    for position in positions:
        m = re.match(pos_regex, position)
        parts = m.groups()
        ret = int(parts[0]) + float(parts[1]) / 60 + float(parts[2]) / 3600
        if parts[3] in ('W','S'):
            ret *= -1
        lat_lon.append(ret)
    return lat_lon

@register.inclusion_tag('includes/google-map.html')
def course_map(position, description):
    try:
        (lat, lon) = convert(position)
    except:
        return False
    return {
        'coordinates': '%5f,%5f' % (lat, lon),
        'description': description,
        'key': settings.GOOGLE_API_KEY
    }

