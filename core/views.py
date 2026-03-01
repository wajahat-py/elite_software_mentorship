from django.shortcuts import render, redirect
from .forms import ApplicationForm

def index(request):
    return render(request, 'core/index.html')

def apply(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('scheduling')
    else:
        form = ApplicationForm()
    
    return render(request, 'core/apply.html', {'form': form})

def scheduling(request):
    return render(request, 'core/scheduling.html')
