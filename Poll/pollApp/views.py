from django.shortcuts import render, redirect
from django.http import HttpResponse
from pollApp import models
from pollApp import forms
# Create your views here.


def home(request):
    polls=models.Poll.objects.all()
    context = {
        'poll' : polls
    }
    return render(request, 'pollApp/home.html', context)


def view(request, pk):
    poll=models.Poll.objects.get(id=pk)
    context = {
        'poll' : poll
    }
    return render(request, 'pollApp/view.html', context)

def create(request):
    if request.method == 'POST':
        form=forms.create_poll_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=forms.create_poll_form()
        
    context={
        'form': form
    }
    return render(request, 'pollApp/create.html', context)

def vote(request, pk):
    poll=models.Poll.objects.get(id=pk)
    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'option_1':
            poll.option_1_count+=1
        elif selected_option == 'option_2':
            poll.option_2_count+=1
        elif selected_option == 'option_3':
            poll.option_3_count+=1
        else:
            return HttpResponse(400, 'Invalid Form')
        poll.save()
        return redirect('view',poll.id)
    
    context={
        'poll':poll
    }
    return render(request, 'pollApp/vote.html', context)

