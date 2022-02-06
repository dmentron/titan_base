"""bases URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.views import logout_then_login

from plataforma.views import index_bases, login_user_bases, panel_bases

urlpatterns = [
    path('admin/', admin.site.urls),

    path('plataforma/', index_bases, name='index_bases'),
    path('bases/login/', login_user_bases, name='bases_login'),
    path('panel/bases/', panel_bases, name='panel_bases'),
    url(r'^logout/bases/$', logout_then_login,
        {'next_page': '/plataforma'}, name='logout_bases'),
]
