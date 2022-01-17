"""DeployModel URL Configuration

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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),

    path("res1/", views.res1, name="res1"),
    path("res2/", views.res2, name="res2"),
    path("res3/", views.res3, name="res3"),
    path("res4/", views.res4, name="res4"),
    path("res5/", views.res5, name="res5"),
    path("res6/", views.res6, name="res6"),

    path('tab1/', views.tab1, name="tab1"),
    path('tab2/', views.tab2, name="tab2"),
    path('tab3/', views.tab3, name="tab3"),
    path('tab4/', views.tab4, name="tab4"),
    path('tab5/', views.tab5, name="tab5"),

    path('class1/', views.tablexg, name="tablexg"),
    path('class2/', views.tablerf, name="tablerf"),
    path('class3/', views.tabledt, name="tabledt"),
    path('class4/', views.tableet, name="tableet"),
    path('class5/', views.tablest, name="tablest"),

    path('about/', views.about, name="about"),
    path('team/', views.team, name="team")
]
