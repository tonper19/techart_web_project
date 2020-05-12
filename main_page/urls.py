# Tony Perez 20200512
# manually created
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]
