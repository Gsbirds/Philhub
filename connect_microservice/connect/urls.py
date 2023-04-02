from django.urls import path
from .views import show_profile

urlpatterns = [
    path("profile/",show_profile, name="profile"),

]