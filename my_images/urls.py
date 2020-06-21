from django.urls import path
from .views import *

urlpatterns = [
    path('',Home,name='home'),
    path('category/<int:cid>/',Category_Page,name='category_page'),
]