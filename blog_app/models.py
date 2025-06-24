from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    
    category = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.category}' 
    
class TravelBlogPost(models.Model):
    
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    destination = models.CharField(max_length=80)
    content = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='travel_pics',null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    
    def __str__(self):
        return f'{self.author} - {self.destination}'    
    
    
class Comment(models.Model):
    
    comment = models.TextField()
    post = models.ForeignKey(TravelBlogPost,on_delete = models.CASCADE,related_name='comments')
    author = models.ForeignKey(User,on_delete = models.CASCADE) 
    posted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.comment} on {self.post}'

         