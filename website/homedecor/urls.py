from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),  # Updated to make home the root URL
   path('login', views.admin_login, name='admin_login'),
   path('dashboard/', views.admin_dashboard, name='admin_dashboard'),  # Added admin_dashboard URL
   path('add-product/', views.add_product, name='add_product'),
   path('edit-product/<int:product_id>/', views.edit_product, name='edit_product'),
   path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
   path('about/', views.about, name='about'),  # Added trailing slash
   path('contact/', views.contact, name='contact'),  # Added contact URL
]