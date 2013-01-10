from django.db import models
from django.utils.translation import ugettext as _

class GolfClub(models.Model):
    """Golf club model inluding logo, title, address and other fields"""
    STATUS_CHOICES = (
            ('FOUNDING', _('founding')),
            ('ASSOCIATED', _('associated')),
    )
    title = models.CharField(_('title'), max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField(_('description'))
    logo = models.ImageField(upload_to='logos/', max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ASSOCIATED')

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('golfclub.detail' )

