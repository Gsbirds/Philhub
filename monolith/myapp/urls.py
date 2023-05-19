from django.urls import path, include
from myapp.views import show_page
from myapp.views import api_list_notes, api_notes_detail, showuploads, showfile, contact, show_page_details, api_list_works, api_show_works

urlpatterns = [
    path("",show_page, name="show_page"),
    path("" "<int:id>/",show_page_details, name="show_page_details"),
    path("api/upload/", showfile, name="show_works_form" ),
    path("api/yourworks/", showuploads, name="your_uploads"),
    path("api/searchworks/", api_list_works, name="list_works"),
    path("api/searchworks/<int:id>/", api_show_works, name="show_works"),
    path("api/noteslist", api_list_notes, name="list_notes"),
    path("api/note/<int:id>/", api_notes_detail, name="show_note"),



    path("api/contact/", contact, name="contact" ),

]
