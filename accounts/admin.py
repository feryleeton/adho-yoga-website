from django.contrib import admin
from accounts.models import AdhoUser
from django.contrib.auth.models import Group


class UserAdmin(admin.ModelAdmin):
    model = AdhoUser

admin.site.register(AdhoUser, UserAdmin)
admin.site.unregister(Group)