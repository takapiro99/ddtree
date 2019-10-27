"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from . import views


urlpatterns = [
    #path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("posttest", views.posttest, name="posttest"),
    path("table",views.table,name="table"),
    path("canvas",views.canvas,name="canvas"),
    path("esp/",views.esp,name="esp"),

    path("tree",views.tree, name="tree"),
    path("about",views.about, name="about"),
    path("post",views.post, name="post"),
    path("waitinglist",views.waitinglist, name="waitinglist"),


]
#index
#tree
#about
#post
#waitinglist