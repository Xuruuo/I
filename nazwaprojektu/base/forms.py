from django import forms
from .models import Room
from .models import Computer

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name']

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ('name', 'description', 'room')