from django.urls import path
from . import views

app_namae = 'tweet'

urlpatterns = [
    path('', views.IndexView.as_view(), name='tweetData'),
]
