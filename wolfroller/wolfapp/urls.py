"""wolfroller URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views

app_name = 'wolfapp'
urlpatterns = [
	path('', views.index, name='index'),
	path('delete/<str:pk>/', views.delete, name="delete"),
	path('roll/', views.roll, name="roll"),
	path('wolfcount/<str:direction>/', views.wolfcounter, name="wolfcounter"),
	path('updatetoggle/<str:pk>/', views.update_toggle, name="update_toggle"),
	path('updatelock/<str:pk>/', views.update_lock, name="update_lock"),
	path('login/', views.loginPage, name="loginPage"),
	path('logout/', views.logoutPage, name="logoutPage"),
	path('register/', views.register, name="register"),

]
