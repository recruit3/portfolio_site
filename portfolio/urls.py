from django.urls import path
from . import views   # ← これだけ

urlpatterns = [
    path('', views.index),
    path('projects/', views.projects),
    path('projects/ai_board/', views.ai_board),
    path('projects/ai_chat/', views.ai_chat),
    path('projects/mysite/', views.mysite),
]