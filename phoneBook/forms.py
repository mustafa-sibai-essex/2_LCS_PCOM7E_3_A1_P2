from django import forms


class UserForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=50)
    email = forms.CharField(max_length=150)
