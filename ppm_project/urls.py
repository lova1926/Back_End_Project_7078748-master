from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # For authentication
    path('goals/', include('goals.urls')),
    path('training/', include('training.urls')),
]