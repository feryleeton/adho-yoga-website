from django.contrib import admin
from main.models import Message


class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display = ['name',
                    'phone',
                    'message',
                    'created', ]


admin.site.register(Message, MessageAdmin)

admin.site.index_title = "Welcome to AdhoYoga Admin panel"
