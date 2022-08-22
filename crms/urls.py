from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="customer-products"),
    path('customer/', views.customer, name="customer"),
]