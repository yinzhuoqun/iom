"""iom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from iom.views import *

# import server
# import api

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^404/(?P<error>\w+)', notfound),
    url(r'^server/', include('server.urls')),
    url(r'^api/', include('api.urls')),

    url(r'^base/', base),
    url(r'^blank/', blank),
    url(r'^buttons/', buttons),

    url(r'^flot/', flot),
    url(r'^forms/', froms),

    url(r'^grid/', grid),

    url(r'^icons/', icons),
    url(r'^index/', index),
    url(r'^$', index),

    url(r'^login/', login),
    url(r'^logout/', logout),

    url(r'^morris/', morris),

    url(r'^notificions/', notificions),

    url(r'^users/', users),

    url(r'^panels_wells/', panels_wells),

    url(r"^register/", register),

    url(r'^tables/', tables),
    url(r'^test/', test),

    url(r'^typography/', typography),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 导入setting、static 是为 media 用
# from django.conf import settings
# from django.conf.urls.static import static
# urlpatterns = [
#
# # ... the rest of your URLconf goes here ...
#
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
