from django.db import models
from django.utils import timezone
import datetime


class Blog(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_content = models.TextField
    pub_date = models.DateTimeField(' date_published ')




# Create your models here.
