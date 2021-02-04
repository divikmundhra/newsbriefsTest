from django.db import models

# Create your models here.



class NewsModel(models.Model):
    # user = 
    # need to add a foreign key as user, but user model isnt created as of now
    title = models.CharField(max_length=264)
    content = models.TextField()
    img_url = models.CharField(max_length=264) 

    def __str__(self):
        return str(self.title)