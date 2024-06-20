from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.start_workout, name='start_workout'),
    path('update/<int:workout_id>/', views.update_workout, name='update_workout'),
    path('stop/<int:workout_id>/', views.stop_workout, name='stop_workout'),
    path('<int:workout_id>/', views.workout_detail, name='workout_detail'),
]
