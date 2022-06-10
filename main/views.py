from django.shortcuts import render, redirect

from main.forms import MessageForm
from main.models import Message


def home(request):
    return render(request, 'main/index.html')


def classes(request):
    return render(request, 'main/classes.html')


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            Message.objects.create(name=form_data['name'], phone=form_data['phone'], message=form_data['message'])
            return redirect('contact')
    else:
        form = MessageForm()

    return render(request, 'main/contact.html', context={
        'form': form
    })