# --------------------------------------|importing all the libraries|----------------------------------------->
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

#  -------------------------------------|Creating register forms with fields|----------------------------------------->

class StudentForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password']
		
# -------------------------------------|Creating register forms with fields|----------------------------------------->
class StudentLoginForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username',  'password']
# -------------------------------------|Creating register forms with fields|----------------------------------------->
class FacultyForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password']        
# -------------------------------------|Creating register forms with fields|----------------------------------------->		
class FacultyLoginForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password']        

class csv_upload(forms.Form):
    file=forms.FileField() # for creating file input  