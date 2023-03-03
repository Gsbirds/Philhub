from django.db import models
from django.contrib.auth.models import User

class News (models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)

class Work (models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    document= models.URLField()
    

class File(models.Model):
    name= models.CharField(max_length=500)
    filepath= models.FileField(upload_to='files/', null=True, verbose_name="")
    author=models.ForeignKey(
        User,
        related_name="file",
        on_delete=models.CASCADE,
        null=True
    )
   