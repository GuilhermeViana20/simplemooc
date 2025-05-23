from django import forms
from django.core.mail import send_mail
from django.conf import settings

from simplemooc.core.mail import send_mail_template

class ContactCourse(forms.Form):
    name = forms.CharField(
        label='Nome',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome Sobrenome'})
    )
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'exemplo@gmail.com'})
    )
    phone = forms.CharField(
        label='Telefone',
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(XX) 9XXXX-XXXX'})
    )
    description = forms.CharField(
        label='Mensagem',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    )

    def send_mail(self):
        subject = 'Formulário de Contato'
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'phone': self.cleaned_data['phone'],
            'message': self.cleaned_data['description']
        }
        template_name = 'core/contact_email.html'
        send_mail_template(
            subject, template_name, context, [settings.CONTACT_EMAIL]
        )