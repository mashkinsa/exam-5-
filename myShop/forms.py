from .models import Product, Order
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    avatar = forms.ImageField()

    class Meta:
        model = User
        fields = ('username', 'email', 'avatar', 'password1')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'avatar')

    avatar = forms.ImageField(label="Аватар", required=False)


class LoginForm(AuthenticationForm):
    pass


class DeleteAccountForm(forms.Form):
    confirm_delete = forms.BooleanField(label='Удалить аккаунт', required=True)


class ProductForm(forms.ModelForm):
    image = forms.ImageField(required=True)

    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'price']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product']
