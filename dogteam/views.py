from django.shortcuts import render, redirect

########## PAGES ##########

def landing(request):
    return render(request, 'landing.html')