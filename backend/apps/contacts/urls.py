from django.urls import path
from .views import ContactFormView

app_name = 'contacts'

urlpatterns = [
    path('', ContactFormView.as_view(), name="index"),
]
