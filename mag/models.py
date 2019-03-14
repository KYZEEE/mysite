from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=32)
    title = models.CharField(max_length=32)
    photo = models.ImageField(upload_to='photo', blank=True, null=True)

    def __unicode__(self):
        return self.name + '(' + self.title + ')'


