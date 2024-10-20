from django.shortcuts import render

# Create your views here.

def index_page(request):
  return render(request, "index.html")

def menu_page(request):
  return render(request, "Menu.html")

def about_page(request):
  return render(request, "About.html")

def booking_page(request):
  return render(request, "Booking.html")
