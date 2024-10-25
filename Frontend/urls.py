from django.urls import path
from Frontend import views

urlpatterns = [
  path('index/', views.index_page, name="index"),
  path('Menu/', views.menu_page, name="Menu"),
  path('About/', views.about_page, name="About"),
  path('Booking/', views.booking_page, name="Booking"),
  path('signup_page', views.signup_page, name="signup_page"),
  path('item_filtered', views.item_filtered, name="item_filtered"),
]