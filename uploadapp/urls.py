from django.urls import path
from . import views

app_name = 'uploadapp'

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
]