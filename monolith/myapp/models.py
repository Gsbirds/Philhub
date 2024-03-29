from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# from six import python_2_unicode_compatible
# from django.utils.encoding import force_text


class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


class Work(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    document = models.URLField()


class Notes(models.Model):
    title = models.CharField(max_length=100)
    text_area = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, related_name="notes", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return str(self.title)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.first_name)


class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class File(models.Model):
    name = models.CharField(max_length=500)
    filepath = models.FileField(upload_to="media/files/")
    favorites = models.ManyToManyField(
        User, related_name="favorites", default=None, blank=True
    )
    author = models.ForeignKey(
        Author, related_name="file", null=True, on_delete=models.CASCADE
    )
    topic = models.ForeignKey(
        Topic, related_name="paper", null=True, on_delete=models.CASCADE
    )

    def get_api_url(self):
        return reverse("show_works", kwargs={"id": self.id})


# class CustomUser(AbstractUser):
#     # Any extra fields would go here
#     def __str__(self):
#         return self.email
