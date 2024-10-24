from django.urls import path
from Backend import views

urlpatterns = [
  path('admin_page/',views.admin_page, name="admin_page")
]