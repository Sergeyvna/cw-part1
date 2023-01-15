from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import ClubForm

def home(request):
    films = Films.objects.all()
    return render(request, 'club_rep_acc/home_page.html',{'films':films})


def bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'club_rep_acc/booking.html', {'bookings':bookings})



def account(request):
    club_reps = ClubRep.objects.all()
    clubs = Club.objects.all()

    context = {'club_reps':club_reps, 'clubs': clubs}
    return render(request, 'club_rep_acc/account.html', context)

def create_rep(request):

    form = ClubForm()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = ClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    context = {'form':form}

    return render(request, 'club_rep_acc/rep_form.html', context)

def update(request, pk):
    club = Club.objects.get(id=pk)
    form = ClubForm(instance=club)

    if request.method == 'POST':
        form = ClubForm(request.POST, instance=club)
        if form.is_valid():
            form.save()
            return redirect('/account')

    context = {'form':form}

    return render(request, 'club_rep_acc/rep_form.html', context)

def delete(request, pk):
    club = Club.objects.get(id=pk)

    if request.method == 'POST':
        club.delete()
        return redirect('/account')
        
    context = {'club':club}
    return render(request, 'club_rep_acc/delete.html', context)
