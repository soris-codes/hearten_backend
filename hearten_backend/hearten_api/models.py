from django.db import models
from django.utils import timezone

class Post(models.Model):
  # Associate post with an author to know which posts a user
  # can edit/delete
  # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
  title = models.CharField(max_length=200)
  body = models.TextField()
  imagePrompt = models.CharField(max_length=300, blank=True )
  textPrompt = models.CharField(max_length=200, blank=True)
  created_on = models.DateTimeField(default=timezone.now)

  class Meta:
    ordering = ['-created_on']
  
  def __str__(self):
    return f'{self.title}'


