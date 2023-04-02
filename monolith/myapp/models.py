from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# from six import python_2_unicode_compatible
# from django.utils.encoding import force_text

class News (models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
                                    
class Work (models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    document= models.URLField()
    

class Notes(models.Model):
    title= models.CharField(max_length=100)
    text_area=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(
        User,
        related_name="notes",
        on_delete=models.CASCADE,
        null=True
    )
    def __str__(self):
        return str(self.title)

# @python_2_unicode_compatible   
class File(models.Model):
    name= models.CharField(max_length=500)
    filepath= models.FileField(upload_to='files/', null=True, verbose_name="")
    favorites=models.ManyToManyField(
        User, related_name='favorites',default=None, blank=True
    )
    author=models.ForeignKey(
        User,
        related_name="file",
        on_delete=models.CASCADE,
        null=True
    )
    
    # def __str__(self):
    #     return force_text(self.pdf_file.path)

    # def __unicode__(self):
    #     return force_text(unicode(self.pdf_file.path))

    # def get_file_path(self):
    #     return force_text(unicode(self.pdf_file.path)) 
    def __str__(self):
        return str(self.name)
    
    def __str__(self):
        return str(self.name)
