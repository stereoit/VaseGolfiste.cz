from django.db import models
from vasegolfiste.clubs.models import GolfClub
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext as _

class GolfCourse(models.Model):
    """Golf course model inluding logo, title, address and other fields"""
    title = models.CharField(_('title'), max_length=100)
    slug = models.SlugField(max_length=100)
    description = RichTextField(_('description'))
    location = models.CharField(max_length=70, blank=True)
    club = models.ForeignKey(GolfClub, blank=True)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('golfcourse.detail' )

