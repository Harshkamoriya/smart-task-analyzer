from django.urls import path
from .views import analyze, suggest

urlpatterns = [
    path('api/tasks/analyze/', analyze),
    path('api/tasks/suggest/', suggest),
]