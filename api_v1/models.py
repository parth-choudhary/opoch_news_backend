from __future__ import unicode_literals

from django.db import models
from mezzanine.generic.models import Keyword
from drum.links.models import Link

# Create your models here.

#
# class LinkImage(models.Model):
#     link = models.OneToOneField(Link)
#     image = models.ImageField(null=True, blank=True)
#
#     def __str__(self):
#         return "%s" % self.keyword


class KeywordImage(models.Model):
    keyword = models.OneToOneField(Keyword, related_name="keyword_image")
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return "%s" % self.keyword
