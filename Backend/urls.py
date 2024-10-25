from django.urls import path
from Backend import views

urlpatterns = [
  path('',views.admin_page, name="admin_page"),
  path('add_menu_page/',views.add_menu_page, name="add_menu_page"),
  path('view_menu/', views.view_menu, name="view_menu"),
  path('add_items/', views.add_items, name="add_items"),
  path('view_items/', views.view_items, name="view_items"),
]