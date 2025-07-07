from django.urls import path
from .views import summarize_chat_view

urlpatterns = [
    path('summarize/', summarize_chat_view, name='summarize-chat'),
]
