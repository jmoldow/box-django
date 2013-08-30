from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
class SimpleFile(models.Model):
  name = models.CharField(max_length=256)
  description = models.TextField(blank=True)
  content = models.TextField(blank=True)
  owner = models.ForeignKey(User)
  is_public = models.BooleanField(default=False)
  ctime = models.DateTimeField(auto_now_add=True, editable=False)
  mtime = models.DateTimeField(auto_now=True, editable=False)

