
from django.urls import path
from .views import *
urlpatterns = [
    path('all/', allContacts),
    path('one/<int:id>/', oneContact),
]