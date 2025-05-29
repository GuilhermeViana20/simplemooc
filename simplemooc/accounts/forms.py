from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.apps import apps

class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput,
        validators=[validate_password]
    )
    password2 = forms.CharField(
        label='Confirme a Senha',
        widget=forms.PasswordInput
    )

    name = forms.CharField(max_length=100, label='Nome', required=False)
    surname = forms.CharField(max_length=100, label='Sobrenome', required=False)
    email = forms.EmailField(label='E-mail')
    image = forms.ImageField(label='Imagem', required=False)

    class Meta:
        model = apps.get_model('accounts', 'User')
        fields = ('username', 'name', 'surname', 'email', 'image')

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError('As senhas não coincidem.')
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("O campo E-mail é obrigatório.")
        if self.Meta.model.objects.filter(email=email).exists():
            raise forms.ValidationError('Este e-mail já está em uso.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.name = self.cleaned_data.get('name', '')
        user.surname = self.cleaned_data.get('surname', '')
        user.image = self.cleaned_data.get('image', None)

        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
class EditForm(forms.ModelForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email:
            raise forms.ValidationError("O campo E-mail é obrigatório.")

        queryset = self.Meta.model.objects.filter(email=email).exclude(pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError("Este e-mail já está em uso.")
        return email

    image = forms.ImageField(label='Imagem', required=False)
    class Meta:
        model = apps.get_model('accounts', 'User')
        fields = ['name', 'surname', 'username', 'email', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }