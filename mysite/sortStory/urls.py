from django.urls import path
from . import views

app_name = 'sortStory'
urlpatterns = [
    path('', views.index, name='index'),
]
