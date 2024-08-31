from django.urls import path
from .views import HomeView, OrderView, ProductDescriptionDetailView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('order', OrderView.as_view(), name="order"),
    path('product-description/<slug:slug>/', ProductDescriptionDetailView.as_view(), name='product-description'),
]
