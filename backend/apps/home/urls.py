from django.urls import path
from .views import HomeView, OrderView, ProductDescriptionDetailView, ProductDetailView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('<slug:slug>', ProductDetailView.as_view(), name="product"),
    path('order', OrderView.as_view(), name="order"),
    path('product-description/<int:pk>/', ProductDescriptionDetailView.as_view(), name='product-description'),
]
