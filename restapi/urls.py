
from django.urls import path
from .views import *
urlpatterns = [
    path('all/', allContacts),
    path('one/<int:id>/', oneContact),
    path('student/', allStudent),
    path('oneStudent/<int:id>/', oneStudent),
]