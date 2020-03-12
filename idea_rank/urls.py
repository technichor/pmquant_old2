from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.idea_list, name='idea_list'),
    path('idea/<int:idea_id>/', views.idea_detail, name='idea_detail'),
    path('', views.index, name='index')
]