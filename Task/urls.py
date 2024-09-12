from django.urls import path
from .views import TaskAPIView

urlpatterns = [
    path('task/', TaskAPIView.as_view(), name='task'),
]