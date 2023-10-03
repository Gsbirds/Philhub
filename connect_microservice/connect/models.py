from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class FileVO(models.Model):
    import_href = models.CharField(max_length=200, unique=True, null=True)
    name = models.CharField(max_length=500)

    # filepath= models.FileField(upload_to='files/', null=True, verbose_name="")
    # favorites=models.ManyToManyField(
    #     User, related_name='favorite',default=None, blank=True
    #  )
    # author=models.ForeignKey(
    #     User,
    #     related_name="filevo",
    #     on_delete=models.CASCADE,
    #     null=True
    # )
    def __str__(self):
        return str(self.name)


class Friend(models.Model):
    name = models.CharField(max_length=200)
    paper = models.ForeignKey(
        FileVO,
        related_name="friend",
        on_delete=models.CASCADE,
        null=True,
    )
    collab = models.FileField(upload_to="files/", null=True, verbose_name="")

    def __str__(self):
        return str(self.name)


class Profile(models.Model):
    picture = models.URLField(max_length=500, null=True)
    name = models.CharField(max_length=200)
    paper = models.ForeignKey(
        FileVO, related_name="profile", on_delete=models.CASCADE, null=True
    )
    favorites = models.ManyToManyField(
        User, related_name="profile", default=None, blank=True
    )

    def __str__(self):
        return str(self.name)


class Collab(models.Model):
    title = models.CharField(max_length=200)
    paper = models.FileField(upload_to="files/", null=True, verbose_name="")
    author = models.ForeignKey(
        User, related_name="collab", on_delete=models.CASCADE, null=True
    )
