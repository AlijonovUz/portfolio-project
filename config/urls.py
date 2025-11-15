from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('send-message/', SendView.as_view(), name='send-message')
]