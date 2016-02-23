from django.db import models


# Create your models here.

class Gig(models.Model):
    gig_date = models.DateTimeField('Date')
    venue = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, default='none')

class Bio(models.Model):
    text = models.TextField()
    
class Video(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=250)
    active = models.BooleanField(default=False)
    
    def __unicode__(self):
        return u'%s' % (self.name)

    