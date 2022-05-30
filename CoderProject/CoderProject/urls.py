from django.contrib import admin
from django.urls import path, include
from CoderProject.views import using_loader
from AppCoder import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loader/',using_loader),
    path('AppCoder/',include('AppCoder.urls'))
]
