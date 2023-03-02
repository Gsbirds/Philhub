from django.urls import path
from myapp.views import show_page
from myapp.views import show_works_page, works_form

urlpatterns = [
    path("",show_page, name="show_page"),
    path("Published",show_works_page, name="show_works_page"),
    path("upload/", works_form, name="show_works_form" )
]