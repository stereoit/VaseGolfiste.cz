from django.db import models

# Create your models here.
class FrontImage(models.Model):
    """Represents one fron image"""
    title = models.CharField(max_length=100)
    path = models.FileField(upload_to='front-images', max_length=100)

    def __unicode__(self):
        return u'{0}'.format(self.title)

