from django.contrib import admin
from django.urls import re_path , include

# from django.urls import re_path as re_path ,include

urlpatterns = [
    re_path (r'^admin/$', admin.site.urls),
    re_path (r'^',include('homepage.urls')),
    
    
]
