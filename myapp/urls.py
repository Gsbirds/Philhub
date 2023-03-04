from django.urls import path
from myapp.views import show_page
from myapp.views import show_works_page, showuploads, showfile

urlpatterns = [
    path("",show_page, name="show_page"),
    path("Published",show_works_page, name="show_works_page"),
    path("upload/", showfile, name="show_works_form" ),
    path("yourworks/", showuploads, name="your_uploads")
]
