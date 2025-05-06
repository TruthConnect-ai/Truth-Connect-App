from django.urls import path
from .views import analyze_view

urlpatterns = [
    path('', analyze_view, name='analyze'),
]
