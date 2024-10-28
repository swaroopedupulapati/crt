from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(max_length=100,label="Enter email : ")
    password = forms.CharField(max_length=100,
                               label="Enter password : ",
                               widget=forms.PasswordInput
                               )
    