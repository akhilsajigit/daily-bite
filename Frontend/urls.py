from django.urls import path
from Frontend import views

urlpatterns = [
  path('', views.index_page, name="index"),
  path('Menu/', views.menu_page, name="Menu"),
  path('About/', views.about_page, name="About"),
  path('Booking/', views.booking_page, name="Booking")
]