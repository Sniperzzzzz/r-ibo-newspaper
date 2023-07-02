from django.db import models
from django.contrib.auth.models import User

# User used for main account login and etc. 

class U(models.Model):
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    is_subscribed = models.BooleanField()

# model U is used for account management and subscription to the services. 

# Create your models here.
class Article(models.Model):
    article_id = models.UUIDField()
    title = models.TextField()
    author = models.TextField()
    date_published = models.DateTimeField()
    #image = models.ImageField(null=True)
    textual_content = models.TextField()
    description = models.TextField(null=True)

    def __str__(self):
        return str(self.article_id)