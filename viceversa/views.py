from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def revers(request):
    user_text = request.GET['user_text']
    revers_text = user_text[::-1]
    kol = len(user_text.split())
    return render(request, 'revers.html', {'use': user_text, 'rev': revers_text, 'k': kol})
