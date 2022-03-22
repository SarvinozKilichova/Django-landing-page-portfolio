from pyexpat import model
from django.db import models
from django.shortcuts import reverse
import datetime
from django.utils.translation import gettext as _


year = list((r,r) for r in range(1984, datetime.date.today().year+1))

def current_year():
    return datetime.date.today().year


class About(models.Model):
  bio = models.TextField(_('bio'))
  picture = models.ImageField(upload_to='images/user', null=True, verbose_name="") 

  def __str__(self):
    return str(self.bio)

class Project(models.Model):
  text = models.CharField(_('text'), max_length=100)
  picture = models.ImageField(upload_to='images/projects', null=True, verbose_name="") 

  def __str__(self):
    return str(self.text)    

class Experience(models.Model):
  title =  models.CharField(_('title'), max_length=200, unique=True)
  company_name =  models.CharField(_('company_name'),max_length=200, unique=True)
  year = models.IntegerField(_('year'), choices=year, default=current_year)
  content = models.TextField(_('content'),)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  

  def __str__(self):
    return self.title

  
  def get_absolute_url(self):
        return reverse('main')

class Education(models.Model):
  title =  models.CharField(_('title'), max_length=200, unique=True)
  education_place =  models.CharField(_('education'), max_length=200, unique=True, null=True)
  year = models.IntegerField(_('year'), choices=year, default=current_year)
  content = models.TextField(_('content'),)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  

  def __str__(self):
    return self.title

  
  def get_absolute_url(self):
        return reverse('main')        
          


