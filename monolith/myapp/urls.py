from django.urls import path, include
from myapp.views import show_page
from myapp.views import showuploads, showfile, contact, make_notes, edit_post, favorites_add, favorites_list, show_page_details, api_list_works, api_show_works

urlpatterns = [
    path("",show_page, name="show_page"),
    path("" "<int:id>/",show_page_details, name="show_page_details"),
    path("upload/", showfile, name="show_works_form" ),
    path("yourworks/", showuploads, name="your_uploads"),
    path("searchworks/", api_list_works, name="list_works"),
    path("searchworks/<int:id>/", api_show_works, name="show_works"),



    path("contact/", contact, name="contact" ),
    # path("notes/", see_notes, name="see_notes"),
    path("notes/",make_notes, name="make_notes"),
    path("notes/<int:id>/", edit_post, name="edit_notes"),
    path("fav/<int:id>/", favorites_add, name="favorites_add"),
    path("fav_list/<int:id>/", favorites_list, name="favorites_list"),
]
