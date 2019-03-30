from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets, permissions

class PostViewSet(viewsets.ModelViewSet):
  permissions_classes = [
    permissions.IsAuthenticated
    # permissions.AllowAny
  ]

  serializer_class = PostSerializer
  
  # Return only the posts belonging to the user
  def get_queryset(self):
    return self.request.user.posts.all()
  # queryset = Post.objects.all()

  # When a post is created, set the author field to the user that is creating the post
  def perform_create(self, serializer):
    serializer.save(author=self.request.user)

  


