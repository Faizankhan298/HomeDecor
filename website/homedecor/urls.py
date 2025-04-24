from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),  
   path('login', views.admin_login, name='admin_login'),
   path('dashboard/', views.admin_dashboard, name='admin_dashboard'),   
   path('add-product/', views.add_product, name='add_product'),
   path('edit-product/<int:product_id>/', views.edit_product, name='edit_product'),
   path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
   path('about/', views.about, name='about'),   
   path('contact/', views.contact, name='contact'),   
   path('chatbot-response/', views.chatbot_response, name='chatbot_response'),
]