# importing forms module
# django forms is used to create ready-made form
# incase you do alot of modification in forms do not use django forms
# instead create forms manually
from django import forms
# importing auth_user model
from django.contrib.auth.models import User
# UserCreationForm is in-built class of django 
from django.contrib.auth.forms import UserCreationForm

# DEMO FORM
# StudentForm is a user-defined class
# StudentForm is inheriting Form class 
class StudentForm(forms.Form):
    # below data members will become forms input fields
    Name = forms.CharField(max_length=50)
    Roll_Number = forms.IntegerField()
    Percentage = forms.IntegerField()

'''--------------------------------------------------------------'''    

# when the no. of form fields == no. of model columns you can use inbuilt model to create form 
# using UserCreationForm Class
class UserForm(UserCreationForm):
    class Meta:
        # using User model to create form fields
        model = User
        # these are the form fields & also column of auth_user table
        fields = ['username','first_name','last_name','email']