from django.contrib import admin
from schedule.models import Activity, Day

# Register your models here.


class ActivityAdmin(admin.ModelAdmin):
    model = Activity
    ordering = ['day', 'start_time']
    list_display = ['title',
                    'category',
                    'day',
                    'start_time',
                    'end_time',
                    'trainer',
              ]
    fields = ['title',
                    'category',
                    'day',
                    'start_time',
                    'end_time',
                    'trainer',
              ]




admin.site.register(Activity, ActivityAdmin)