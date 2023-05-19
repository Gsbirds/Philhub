from django.contrib import admin
from myapp.models import News
from myapp.models import Work, File, Notes, Author, Topic
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# from .forms import CustomUserChangeForm, CustomUserCreationForm
# from .models import CustomUser
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display=(
        "title",
        "description",
        "id",
    )
admin.site.register(News, NewsAdmin)

class WorkAdmin(admin.ModelAdmin):
    list_display=(
        "title",
        "description",
        "id",
        "document"
    )
admin.site.register(Work, NewsAdmin)

class FileAdmin(admin.ModelAdmin):
    list_display=(
        "name",
        "filepath",
        "id"
    )
admin.site.register(File, FileAdmin)

class NotesAdmin(admin.ModelAdmin):
    list_display=(
        "title",
        "text_area",
        "author",
        "id"
    )
admin.site.register(Notes, NotesAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display=(
        "first_name",
        "last_name"
    )
admin.site.register(Author, AuthorAdmin)

class TopicAdmin(admin.ModelAdmin):
    list_display=(
       "name",
    )
admin.site.register(Topic, TopicAdmin)

# class CustomUserAdmin(UserAdmin):    
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email']
# admin.site.register(CustomUser, CustomUserAdmin)