from django.urls import path
from basics.views import HomeTemplate, AboutTemplate, ContactTemplate


urlpatterns = [
    path('', HomeTemplate.as_view(), name='home-template'),
    path('about/', AboutTemplate.as_view(), name='about-template'),
    path('contact/', ContactTemplate.as_view(), name='contact-template'),
]
