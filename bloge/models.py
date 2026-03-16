# pylint: disable=missing-class-docstring
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField  # noqa: F401
from ckeditor_uploader.fields import RichTextUploadingField  # type: ignore
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe  # noqa: F401


class Category(models.Model):
    STATUS_CHOICES = (('published', 'Published'), ('draft', 'Draft'))
    category = models.CharField(max_length=100)


class Album(models.Model):
    STATUS_CHOICES = (('published', 'Published'), ('draft', 'Draft'))

    title = models.CharField(max_length=200)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to='blog_posts/images/')
    category = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='blog_posts/images/', default='auther_profile_picture')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    slug = models.SlugField(max_length=200, unique=True)

    likes = models.ManyToManyField(User, related_name='album_likes', blank=True)

    def total_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title






class Post(models.Model):
    STATUS_CHOICES = (('published', 'Published'), ('draft', 'Draft'),)
    title = models.CharField(max_length=200)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to='blog_posts/images/')
    category = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='blog_posts/images/', default='auther_profile_picture')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    slug = models.SlugField(max_length=200, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



class AboutUs(models.Model):
    STATUS_CHOICES = (('published', 'Published'), ('draft', 'Draft'),)
    title = models.CharField(max_length=200)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to='about/')
    publish_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')
    telephone_nr = models.CharField(max_length=100)
    video_link = models.URLField(max_length=100)

    def __str__(self):
        return self.title

class Member(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='chefs/')
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class EventMission(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='event/', default="testing.jpg")

    def __str__(self):
        return self.name

class Gallery(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallary/')
    description = models.CharField(default="God is the Might", max_length=255)

    def __str__(self):
        return self.name



class MenuOver(models.Model):
    STATUS_CHOICES = (('published', 'Published'), ('draft', 'Draft'),)
    title = models.CharField(max_length=200)
    icon_class = models.CharField(max_length=255, default="bi bi-clipboard-data")
    description = RichTextUploadingField()

    def __str__(self):
        return self.title
