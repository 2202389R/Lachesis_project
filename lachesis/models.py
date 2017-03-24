from __future__ import unicode_literals
from django.utils import timezone

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
		
class Genre(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        if self.views < 0:
            self.views = 0
        self.slug = slugify(self.name)
        super(Genre, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Story(models.Model):
    genre = models.ForeignKey(Genre)
    title = models.CharField(max_length=128)
    author = models.ForeignKey(User, null=True, blank=False)
    votes = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Stories'
	
    def save(self, *args, **kwargs):
        if self.votes < 0:
            self.votes =0
        self.slug = slugify(self.title)
        super(Story, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.title
        

class Segment(models.Model):
    segment_number = models.CharField(max_length=64)
    story = models.ForeignKey(Story)
    segment_text = models.TextField(max_length=10000)
    pub_date = models.DateTimeField(default=timezone.now)
    closed = models.BooleanField(default=False)
    option1 = models.TextField(max_length=1000)
    option2 = models.TextField(max_length=1000)
    option1votes = models.IntegerField(default=0)
    option2votes = models.IntegerField(default=0)
    #slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if self.option1votes < 0:
            self.option1votes = 0
		
        if self.option2votes < 0:
            self.option2votes = 0

        self.slug = slugify(self.segment_number)
        super(Segment, self).save(*args, **kwargs)
    
    def voting_period(self):
        if self.pub_date >= timezone.now() - datetime.timedelta(days=1):
            self.closed = True
    
    def __str__(self):
        return self.segment_number


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

class UserSegment(models.Model):
    user = models.ForeignKey(User)
    option = models.CharField(max_length=1)
    story = models.ForeignKey(Story)
    segment = models.ForeignKey(Segment)
	

