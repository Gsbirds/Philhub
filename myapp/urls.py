from django.urls import path
from myapp.views import show_page
from myapp.views import showuploads, showfile, search_results, contact, make_notes, edit_post

urlpatterns = [
    path("",show_page, name="show_page"),
    path("upload/", showfile, name="show_works_form" ),
    path("yourworks/", showuploads, name="your_uploads"),
    path("searchworks/", search_results, name="search"),
    path("contact/", contact, name="contact" ),
    # path("notes/", see_notes, name="see_notes"),
    path("notes/",make_notes, name="make_notes"),
    path("notes/<int:id>/", edit_post, name="edit_notes")
]
