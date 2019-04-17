from django.db import models
from django.conf import settings
import post.models



# Create your models here.
class Hashtag(models.Model):
    name = models.CharField(max_length=50)
    hid = models.ManyToManyField(post.Post,default=1, blank=False, null=False)

    def __str__(self):
        return self.name
