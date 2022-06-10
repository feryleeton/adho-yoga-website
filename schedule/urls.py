from schedule.initialize_models import init_schedule_models
from django.conf.urls.static import static
from django.urls import path

from schedule import views


urlpatterns = [
    path('', views.schedule, name='schedule'),
]

init_schedule_models()