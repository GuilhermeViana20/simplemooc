from django.shortcuts import render
from django.http import HttpResponse
from simplemooc.core.forms import ContactCourse

def home(request):
    return render(request, 'home.html')

def contact(request):
    form = ContactCourse(request.POST or None)
    is_valid = False

    if request.method == 'POST' and form.is_valid():
        form.send_mail()
        is_valid = True
        form = ContactCourse()

    return render(request, 'contact.html', {
        'form': form,
        'is_valid': is_valid,
    })