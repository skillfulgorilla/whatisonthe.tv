from django.db import models

class BroadCast(models.Model):

    programme = models.ForeignKey('Programme', blank=True, null=True)
    channel = models.ForeignKey('Channel', blank=True, null=True)
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    blurb = models.TextField(blank=True)

    def __unicode__(self):
        return "%s %s" % (self.start_time, self.end_time)

class Channel(models.Model):

    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    xml_id = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

class Programme(models.Model):

    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

