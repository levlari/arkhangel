from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('', include('test_arh.urls', namespace='test_arh')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
