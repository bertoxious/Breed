from django import forms 
from cows.models import CommentonCattle


class AddCattleComment(forms.ModelForm):

	class Meta:
		model = CommentonCattle
		fields = '__all__'
		exclude = ['cattle','date_added']
		
