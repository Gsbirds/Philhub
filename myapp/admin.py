from django.contrib import admin
from myapp.models import News
from myapp.models import Work
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

