from django.urls import path
from .views import *

urlpatterns = [
    path('', CoinsView.as_view(), name='index'),
    path('group/<str:slug>/', PostByGroup.as_view(), name="group"),
    path('coin/<str:slug>/', CoinDetailView.as_view(), name="coin"),
    path('search/', Search.as_view(), name="search"),
]