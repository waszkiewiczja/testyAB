from django.db.models import fields
from rest_framework import serializers
from mojetesty.models import MyTests

class MyTestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyTests
        fields = ['sygnal_link1', 'sygnal_link2', 'sygnal_wynik', 'sygnal_konwersja1', 'sygnal_konwersja2']