from django.shortcuts import render

# Create your views here.

def admin_page(request):
  return render(request, "admin-page.html")

def add_menu_page(request):
  return render(request, "add-menu.html")

def view_menu(request):
  return render(request, "view-menu.html")

def add_items(request):
  return render(request, "add-items.html")

def view_items(request):
  return render(request, "view-items.html")