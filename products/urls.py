from django.contrib import admin
from django.urls import path, include
from .views import main_page, ProductList, ProductDetail, PotDetail, PotList
urlpatterns = [
    path('', main_page, name="main_page_url"),
    path('list', ProductList.as_view(), name='list_view_url'),
    path('pot-list', PotList.as_view(), name='pot_list_view_url'),
    path('p/<pk>', ProductDetail.as_view(), name='detail_view_url'),
    path('pot/<pk>', PotDetail.as_view(), name='pot_detail_url')
]