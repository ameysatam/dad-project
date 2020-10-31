from django.urls import path, include
from dadwebsite import views

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),

]