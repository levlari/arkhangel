"""arkhangel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from . import views

app_name = 'test_arh'

urlpatterns = [
    #path('<int:question_id>/', views.test_arh, name='test_arh'),
    path('test_arh/', views.test_arh, name='test_arh'),
    path('', views.test_arh_start, name='test_arh_start'),
    path('final/', views.test_arh_final, name='test_arh_final'),
]
