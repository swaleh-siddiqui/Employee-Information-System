"""
URL configuration for Employee_Management_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from employee.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = "index"),
    path('register', register, name = "register"),
    path('emp_login', emp_login, name = "emp_login"),
    path('emp_home', emp_home, name = "emp_home"),
    path('profile', profile, name = "profile"),
    path('logout', Logout, name = "logout"),
    path('emp_edit_profile', emp_edit_profile, name = "emp_edit_profile"),
    path('emp_change_password', emp_change_password, name = "emp_change_password"),
    path('admin_login', admin_login, name = "admin_login"),
    path('admin_home', admin_home, name = "admin_home"),
    path('logoutadmin', Logoutadmin, name = "logoutadmin"),
    path('admin_change_password', admin_change_password, name = "admin_change_password"),
    path('admin_emp_details', admin_emp_details, name = "admin_emp_details"),
    path('admin_profile', admin_profile, name = "admin_profile"),
    path('admin_signup', admin_signup, name = "admin_signup"),
    path('login', alllogin, name = "login"),
    path('delete_emp/<int:id>', delete_emp, name = "delete_emp"),
    path('admin_edit_emp/<int:id>',admin_edit_emp , name = "admin_edit_emp"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
