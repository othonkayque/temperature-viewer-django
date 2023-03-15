from django.contrib import admin
from django.urls import path
from app_show_temperature.views import home, show_temp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('temp/', show_temp, name="show_temp"),
]
