from django.contrib import admin
from django.urls import path, include
from . import views  # Importa il modulo views dal progetto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('training/', include('training.urls')),
    path('goals/', include('goals.urls')),
]
