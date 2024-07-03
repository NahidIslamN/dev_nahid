from django.urls import path
from viewer.views import *


urlpatterns = [
    path('about/', AboutMe.as_view(), name='aboutpage'),
    path('resume/', MyResume.as_view(), name='resume'),
    path('portfolio/', MyPortfolio.as_view(), name='portfolio'),
    path('services/', MyService.as_view(), name='services'),
    path('contacts/', MyContact.as_view(), name='contacts'),
    
]