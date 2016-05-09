# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from localflavor.us.models import USStateField
from django.db import models
# Create Manager Model
'''
class BookManager(models.Manager):
    def title_count(slef,keyword):
        return slef.filter(title__icontains=keyword).count()
'''
class MaleManager(models.Manager):
    def get_query_set(self):
        return super(MaleManager,self).get_query_set().filter(sex='M')
class FemaleManager(models.Manager):
    def get_query_set(slef):
        return super(FemaleManager,self).get_query_set().filter(sex='F')

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):	# return self.name's Unicode object
    	return self.name
    class Meta:
    	ordering = ['name']

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True,verbose_name='电子邮箱')   # allow empty

    def __unicode__(self):
    	return u'%s %s' % (self.first_name,self.last_name)
    class Meta:
    	ordering = ['first_name']

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    num_pages = models.IntegerField(blank=True,null=True)
    #objects = BookManager()

    def __unicode__(self):
    	return self.title
    class Meta:
    	ordering = ['title']

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1,choices=(('F','Female'),('M','Male')))
    # birth_date = models.DateField(blank=True,null=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = USStateField()  # this is U.S.-centric...
    '''
    people = models.Manager()
    men = MaleManager()
    women = FemaleManager()
    def __unicode__(self):
        return self.first_name
    '''
    def baby_boomer_staus(slef):
        import datetime
        if datetime.date(1945,8,1) <= self.birth_date <= datetime.date(1964,12,31):
            return 'Baby Boomer'
        if self.birth_date < datetime.date(1945,8,1):
            return 'Pre Boomer'
        return 'Post Boomer'
    def is_midwestern(self):
        '''Jude MW'''
        return self.state in('IL','WI', 'MI', 'IN', 'OH', 'IA', 'MO')
    def _get_full_name(self):
        '''Return Full name'''
        return u'%s %s' % (self.first_name,self.last_name)
    full_name = property(_get_full_name)