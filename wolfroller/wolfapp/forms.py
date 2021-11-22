from django.forms import ModelForm
from .models import Player
from django import forms


class PlayerForm(ModelForm):

	name = forms.CharField(
		max_length=255,
		widget=forms.TextInput(attrs={'autofocus': True})
	)

	class Meta:
		model = Player
		fields = ['name']

