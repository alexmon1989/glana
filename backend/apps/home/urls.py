from django.urls import path
from .views import HomeView, OrderView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('order', OrderView.as_view(), name="order"),
]
