from django import forms
from django.contrib.auth.forms import UserChangeForm , PasswordChangeForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model() # username은 unique하기 때문에 수정하지 않는다.
        fields = ['email', 'first_name', 'last_name',]

class UserPassChangeForm(PasswordChangeForm):
    class Meta:
        model = get_user_model()
        fields =  ['password',]
