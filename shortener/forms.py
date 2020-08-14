from django import forms

class LinktoShorten (forms.Form):
	full_URL = forms.URLField(label='URL', widget=forms.TextInput(attrs={'class': "sr-only"})) 

