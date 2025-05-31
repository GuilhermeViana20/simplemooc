from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import (UserCreationForm, PasswordChangeForm, SetPasswordForm)
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse

from .forms import RegisterForm, EditForm, PasswordResetForm
from .models import PasswordReset

User = get_user_model()

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username,
                password=form.cleaned_data['password']
            )
            login(request, user)
            return redirect('core:home')
        else:
            print("Erros do formulário:", form.errors)
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')

def password_reset(request):
    template_name = 'accounts/password_reset.html'
    context = {}
    form = PasswordResetForm(request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)

def password_reset_confirm(request, key):
    template_name = 'accounts/password_reset_confirm.html'
    context = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)

@login_required
def edit(request):
    context = {}
    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditForm(instance=request.user)
            context['success'] = True
    else:
        form = EditForm(instance=request.user)
    context['form'] = form
    return render(request, 'accounts/edit.html', context)

@login_required
def edit_password(request):
    context = {}
    context['show'] = True
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
            context['show'] = False
    else:
        form = PasswordChangeForm(user=request.user)
        context['success'] = False
    context['form'] = form
    context['login_url'] = reverse('accounts:login')
    return render(request, 'accounts/edit_password.html', context)