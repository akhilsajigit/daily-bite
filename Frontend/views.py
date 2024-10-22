from django.shortcuts import render


# Create your views here.

def index_page(request):
    return render(request, "index.html")


def menu_page(request):
    return render(request, "menu.html")


def about_page(request):
    return render(request, "about.html")


def booking_page(request):
    return render(request, "booking.html")

def signup_page(request):
    return render(request, "signUp.html")

def item_filtered(request):
    return render(request, "item-filtered.html")