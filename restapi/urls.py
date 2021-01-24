
from django.urls import path
from .views import *
urlpatterns = [
    path('all/', allContacts, name = 'all'),
    path('one/<int:id>/', oneContact),
    path('student/', allStudent),
    path('oneStudent/', oneStudent),
    path('detailsStudent/<int:id>/', detailsStudent),
    path('studentsClass/<int:id>/', studentsClass),
    path('subject/<int:id>/', subject),
    path('test/', test, name= 'test'),
]