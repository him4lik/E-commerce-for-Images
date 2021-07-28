from django import forms
from .models import Image

class guest_checkout_form(forms.Form):
	name=forms.CharField()

class post_to_sell_form(forms.ModelForm):
	class Meta:
		model=Image
		fields=['file', 'artist', 'amount']
		widgets={'artist': forms.HiddenInput()}