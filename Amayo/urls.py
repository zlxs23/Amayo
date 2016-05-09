"""Amayo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from Amayo.views import hello,CurrentTime,hours_ahead,display_meta
from books import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$',hello),
    url(r'^time/$',CurrentTime),
    url(r'^time/plus/(\d{1,2})/$',hours_ahead),
    url(r'^meta/$',display_meta),
    url(r'^form/$',views.search_form),
    url(r'^search/$',views.search),
    url(r'^contact/$',views.contact),
    url(r'^contact/thanks/$',views.contact),
    url(r'^publisher/$',views.PublisherList.as_view()),
    url(r'^books/([\w\-]+)/$',views.PublisherBookList.as_view())
]
