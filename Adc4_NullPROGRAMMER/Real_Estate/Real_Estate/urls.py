
from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
]
