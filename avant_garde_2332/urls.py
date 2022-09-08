from django.contrib import admin
from django.urls import include,path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('articles/', include('articles.urls')), # Need to finish this video https://youtu.be/W5Gjcs6QwEs
    path('about/', views.about),
    path('', views.homepage),
    path('api/',views.api),
]
