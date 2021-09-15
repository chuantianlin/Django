from django.db import models
from django.contrib.auth.models import User
from django.views import generic
# Create your models here.
#models contains the data field
#modlesfield of data
STATUS=((0,'Draft'),(1,'Publish'))
class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    date_created=models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=200,unique=True)#.com/dog/....
    author=models.ForeignKey(to=User,on_delete=models.CASCADE)#get data from other table # delete the post will be delated 
    status=models.IntegerField(choices=STATUS,default=0)# publish or delete

    def __str__(self):
        return self.title
#user model viw html
