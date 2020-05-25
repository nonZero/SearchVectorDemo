from django.contrib import admin
from django.urls import path

from stuff import views

urlpatterns = [
    path('', views.Home.as_view()),
    path('admin/', admin.site.urls),
]
