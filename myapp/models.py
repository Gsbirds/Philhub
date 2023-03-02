from django.db import models

class News (models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)

class Work (models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    document= models.URLField()
