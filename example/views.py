from django.shortcuts import render, HttpResponse
from datetime import datetime
from example.models import Suggestions
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        "variable" : "come on bitches surf on it"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("this is home page")

def about(request):
    return render(request, 'about.html')
    
def projects(request):
    return render(request, 'projects.html')

def suggestions(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        suggestions = request.POST.get('suggestions')
        suggestions = Suggestions(name=name, email=email, phone=phone, suggestions=suggestions,date=datetime.today())
        suggestions.save()
        messages.success(request, 'You precious suggestion has been sent to me and I will surely work on it.')

    return render(request, 'suggestions.html')