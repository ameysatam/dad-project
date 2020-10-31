from django.shortcuts import render
from django.views.generic import CreateView
from dadwebsite.models import Users

# Create your views here.
class IndexView(CreateView):
    template_name = 'index.html'
    fields = ('name', 'email', 'message')
    model = Users




