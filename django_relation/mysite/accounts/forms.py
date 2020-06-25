from django import forms
from django.contrib.auth.forms import UserChangeForm , PasswordChangeForm, UserCreationForm
from django.contrib.auth import get_user_model


# 항상 활성화된 모델
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model() # username은 unique하기 때문에 수정하지 않는다.
        fields = ['email', 'first_name', 'last_name',]

class UserPassChangeForm(PasswordChangeForm):
    class Meta:
        model = get_user_model()
        fields =  ['password',]

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        # fields =
