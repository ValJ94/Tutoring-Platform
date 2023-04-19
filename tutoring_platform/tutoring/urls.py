from django.urls import path
from tutoring import views

app_name = 'tutoring'

urlpatterns = [
    path('', views.index, name='index')
]