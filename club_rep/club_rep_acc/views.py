from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'club_rep_acc/home_page.html')

def cinemas(request):
    return render(request, 'club_rep_acc/films.html')

def account(request):
    return render(request, 'club_rep_acc/account.html')
