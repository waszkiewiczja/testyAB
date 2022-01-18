from django.forms import ModelForm, fields
from .models import *

class MyTestForm(ModelForm):
    class Meta:
        model = MyTests
        fields = ['nazwa', 'link1', 'link2', 'active']