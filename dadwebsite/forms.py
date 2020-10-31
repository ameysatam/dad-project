from django import forms
from dadwebsite.models import Users

class IndexContactUs(forms.ModelForm):

    class Meta():
        model = Users
        fields = ('name', 'email', 'message')
