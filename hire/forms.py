from django import forms

class hire_form(forms.Form):
	name=forms.CharField()
	message=forms.CharField()