from django import forms
from .models import CustomerUser


class CustomerUserForm(forms.ModelForm):

    class Meta:
        model = CustomerUser
        fields = ('full_name', 'phone', 'address', 'city', 'username', 'password', )
