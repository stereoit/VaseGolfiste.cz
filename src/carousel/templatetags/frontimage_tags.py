import re
from django.conf import settings
from django import template
from django.shortcuts import get_object_or_404
register = template.Library()
from carousel.models import FrontImage


@register.inclusion_tag('front-images.html')
def front_images(amount=5):
    images = []
    qs = FrontImage.objects.all().order_by('?')
    if len(qs) < amount:
        amount = len(qs)
    for i in range(0,amount):
        images.append(qs[i])
    return {
        'images': images,
    }

