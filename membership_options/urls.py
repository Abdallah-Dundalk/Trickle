from django.urls import path
from . import views

urlpatterns = [
    path('', views.membership_options, name='membership_options'),

]