from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):

  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=True)
  title = models.CharField(max_length=200)
  body = models.TextField()
  imagePrompt = models.CharField(max_length=300, blank=True )
  textPrompt = models.CharField(max_length=200, blank=True)
  created_on = models.DateTimeField(default=timezone.now)

  class Meta:
    ordering = ['-created_on']
  
  def __str__(self):
    return f'{self.title}'


