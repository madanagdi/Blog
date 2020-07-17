from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
 

class Post(models.Model):

    title = models.CharField(max_length = 100,null=True)
    friend = models.ForeignKey(User , on_delete=models.CASCADE,related_name='blog_posts',null = True)
    subject = models.TextField(null=True)
    publish = models.DateTimeField(default=timezone.now)
    pic = models.ImageField(upload_to='Post/images',null = True)
    class Meta:

        ordering = ('-publish',)
 
    def __str__ (self):
        return self.title

# Create your models here.
