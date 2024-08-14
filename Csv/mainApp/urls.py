from django.urls import path
from .views import *

urlpatterns = [
    path('upload/',upload,name='upload'),
    path('items/',item_list_view,name='item-list-view')
]
