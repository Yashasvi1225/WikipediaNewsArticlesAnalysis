from django.urls import path
from . import views

urlpatterns = [
    path('api/trending-topics/', views.get_trending_topics, name='get_trending_topics'),
]
