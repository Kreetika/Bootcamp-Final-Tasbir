from django.db import models
from user_app.models import UserModel

# Create your models here.

class PostModel(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    location = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(UserModel,on_delete=models.CASCADE, related_name = 'posts')
    photo = models.ImageField(upload_to='user_uploads')
    liked_by = models.ManyToManyField(UserModel, related_name='liked_photos', blank=True)
    
    def __str__(self):
        return str(self.created)

class CommentModel(models.Model):
    craeted = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    commented_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    parent_post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments')   
    
     
    
  