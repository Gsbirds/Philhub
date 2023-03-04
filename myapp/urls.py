from django.urls import path
from myapp.views import show_page
from myapp.views import showuploads, showfile, search_results

urlpatterns = [
    path("",show_page, name="show_page"),
    path("upload/", showfile, name="show_works_form" ),
    path("yourworks/", showuploads, name="your_uploads"),
    path("searchworks/", search_results, name="search")
]
