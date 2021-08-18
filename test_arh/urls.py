from django.urls import path
# from django.contrib import admin
from . import views

app_name = 'test_arh'

urlpatterns = [
    path('test_arh/', views.test_arh, name='test_arh'),
    path('', views.test_arh_start, name='test_arh_start'),
    path('final/', views.test_arh_final, name='test_arh_final'),
]
