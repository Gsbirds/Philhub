from django.contrib import admin

from .models import Friend, Profile, Collab, FileVO

# Register your models here.


class FriendAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "paper",
        "collab",
        "id",
    )


admin.site.register(Friend, FriendAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "paper",
        "id",
    )


admin.site.register(Profile, ProfileAdmin)


class CollabAdmin(admin.ModelAdmin):
    list_display = ("title", "paper", "author", "id")


admin.site.register(Collab, CollabAdmin)


class FileVOAdmin(admin.ModelAdmin):
    list_display = ("name", "id")


admin.site.register(FileVO, FileVOAdmin)
