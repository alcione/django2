#from urllib import request

from django.urls import path
from .views import home, AppOs

urlpatterns = [
    path('', home),
    path('AppOs/<int:id>', AppOs),
]


#request > urls > view > model > response