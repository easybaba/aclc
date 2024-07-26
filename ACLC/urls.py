from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', include('management.urls')),
    path('', views.home, name="Home"),
    path('about/', views.about, name="about"),
    path('admin/', admin.site.urls),
    path('service/', views.services, name="services"),
]