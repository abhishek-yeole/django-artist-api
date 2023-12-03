# urls.py

from django.urls import path
from rest_framework import permissions
from .views import WorkListCreateView, RegisterView

urlpatterns = [
    path('api/works/', WorkListCreateView.as_view(), name='work-list-create'),
    path('api/register/', RegisterView.as_view(), name='register'),
]
