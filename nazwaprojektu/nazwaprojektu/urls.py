"""nazwaprojektu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from base import views



def home(request):
    return HttpResponse('homepage')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('computer/', home),
    path('computer/<int:pk>/edit/', views.computer_edit, name='computer_edit'),
    path('computers/<int:room_id>/', views.computer_list, name='computer_list'),
    path('computer/<int:pk>/delete/', views.computer_delete, name='computer_delete'),
]
