from django import forms 
from dogs.models import Dogcomment


class AddDogComment(forms.ModelForm):
	class Meta:
		model = Dogcomment
		fields = '__all__'
		exclude = ['dog',]