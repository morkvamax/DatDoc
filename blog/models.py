from django.db import models
from django.utils import timezone


class KeyWord(models.Model):
    title = models.CharField(max_length=300)
    color = models.CharField(max_length=300, default='rgb(90,90,90)')

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    date = models.DateTimeField()
    publish = models.BooleanField(default=False)
    keywords = models.ManyToManyField('KeyWord', null=True, blank=True)

class Knowledge(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    collapse = models.TextField(null=True, blank=True)

class Competency(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()

class Motivation(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()

class Language(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()

class Project(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()

class Job(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()

class Certificate(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()

