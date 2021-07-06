from django import forms 
from cats.models import CommentonCat


class AddCatComment(forms.ModelForm):

	class Meta:
		model = CommentonCat
		fields = '__all__'
		exclude = ['active','cat','date_added']
		
