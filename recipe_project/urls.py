"""
URL configuration for recipe_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from viggie.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view_receipi,name="home"),
    path('viggie/',view_receipi,name="veggie"),
    path('delete_item/<id>/',delete_item,name="delete"),
    path('update_item/<id>/',update_item,name="update"),
    path('register/',register,name="register"),
    path('login_page/',login_page,name="login"),
    path('logout_page/',logout_page,name="logout"),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
