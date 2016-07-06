from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models


class Slider(models.Model):
    slider_text = models.CharField(max_length=1000, blank=True, null=True)
    slider_image = models.FileField()

    def __unicode__(self):
        return self.slider_text




class Menu(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    base_url = models.CharField(max_length=100, blank=True, null=True)
    data = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class SubMenu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)
    title = models.CharField(max_length=250, null=True, blank=True)
    title2 = models.CharField(max_length=250, null=True, blank=True)
    title3 = models.CharField(max_length=250, null=True, blank=True)
    data = models.TextField(blank=True, null=True)
    data2 = models.TextField(blank=True, null=True)
    data3 = models.TextField(blank=True, null=True)
    image1 = models.FileField(blank=True, null=True)
    image2 = models.FileField(blank=True, null=True)
    image3 = models.FileField(blank=True, null=True)
    image4 = models.FileField(blank=True, null=True)
    image5 = models.FileField(blank=True, null=True)
    image6 = models.FileField(blank=True, null=True)
    image7 = models.FileField(blank=True, null=True)


    def __unicode__(self):
        return unicode(self.title)


class Context(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, blank=True)
    submenu = models.ForeignKey(SubMenu, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=500, blank=True)
    title2 = models.CharField(max_length=500, blank=True)
    title3 = models.CharField(max_length=500, blank=True)
    title4 = models.CharField(max_length=500, blank=True)
    text = models.TextField(null=True, blank=True)
    text2 = models.TextField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)

    def __unicode__(self):
        return self.title


class Question(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    question = models.TextField()
    answer = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.question


class Personal(models.Model):
    name = models.CharField(max_length=250)
    prof = models.CharField(max_length=500, blank=True)
    info = models.TextField()
    image = models.FileField()
    slug = models.SlugField(max_length=40, blank=True)

    def __unicode__(self):
        return self.name


class ArticleContext(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    title2 = models.CharField(max_length=200, blank=True, null=True)
    title3 = models.CharField(max_length=200, blank=True, null=True)
    title4 = models.CharField(max_length=200, blank=True, null=True)
    text1 = models.TextField(blank=True, null=True)
    text2 = models.TextField(blank=True, null=True)
    text3 = models.TextField(blank=True, null=True)
    text4 = models.TextField(blank=True, null=True)
    text5 = models.TextField(blank=True, null=True)
    image1 = models.FileField(blank=True, null=True)
    image2 = models.FileField(blank=True, null=True)
    image3 = models.FileField(blank=True, null=True)
    image4 = models.FileField(blank=True, null=True)
    image5 = models.FileField(blank=True, null=True)
    image6 = models.FileField(blank=True, null=True)
    image7 = models.FileField(blank=True, null=True)

    def __unicode__(self):
        return self.title


class Gallery(models.Model):
    text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.text

class Images(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    image_text = models.CharField(max_length=250, blank=True, null=True)
    image = models.FileField(blank=True, null=True)
