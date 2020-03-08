from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.idea_list, name='idea_list'),
    path('', views.index, name='index')
]