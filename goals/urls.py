from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_goal, name='create_goal'),
    path('<int:pk>/', views.goal_detail, name='goal_detail'),
]
