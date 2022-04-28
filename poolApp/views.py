from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import PollForm
from .models import Poll

# Create your views here.
def index(request):
    polls = Poll.objects.all()
    context = {'polls':polls}
    return render(request, 'pollApp/index.html', context)

def create(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PollForm
    context = {'form':form}
    return render(request, 'pollApp/create.html', context)
    

def vote(request,pollid):
    poll = Poll.objects.get(pk=pollid)
    if request.method == 'POST':
        choice = request.POST['poll']
        if choice == 'option1':
            poll.opt1count +=1
        elif choice == 'option2':
            poll.opt2count +=1
        elif choice == 'option3':
            poll.opt3count +=1
        else:
            return HttpResponse(400,'Invalid Form')
        poll.save()
        return redirect('result', pollid)
    context = {'poll':poll}
    return render(request, 'pollApp/main.html', context)

def result(request,pollid):
    poll = Poll.objects.get(pk=pollid)
    context = {'poll':poll}
    return render(request, 'pollApp/result.html', context)
