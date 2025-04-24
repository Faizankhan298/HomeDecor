from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from .forms import AdminLoginForm, ProductForm
from .models import Product

def home(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')

    products = Product.objects.all()

    if query:
        products = products.filter(title__icontains=query)
    if category:
        products = products.filter(category=category)
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    return render(request, 'Home.html', {
        'products': products,
        'categories': Product.CATEGORY_CHOICES
    })


def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if email == 'Zahir@gmail.com' and password == 'Zahir@123':
                request.session['is_admin_logged_in'] = True
                return redirect('admin_dashboard')
            else:
                messages.error(request, 'Invalid email or password.')
    else:
        form = AdminLoginForm()
    return render(request, 'Admin_Login.html', {'form': form})

def admin_dashboard(request):
    if not request.session.get('is_admin_logged_in'): 
        return redirect('admin_login')
    products = Product.objects.all()
    return render(request, 'Admin_Dashboard.html', {'products': products})

def add_product(request):
    if not request.session.get('is_admin_logged_in'):  
        return redirect('admin_login')
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = ProductForm()
    return render(request, 'Add_Product.html', {'form': form})

def edit_product(request, product_id):
    if not request.session.get('is_admin_logged_in'):  
        return redirect('admin_login')
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request, 'Edit_Product.html', {'form': form, 'product': product})

def delete_product(request, product_id):
    if not request.session.get('is_admin_logged_in'): 
        return redirect('admin_login')
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('admin_dashboard')

def about(request):
    return render(request, 'About.html')

def contact(request):
    return render(request, 'Contact.html')

def chatbot_response(request):
    if request.method == 'GET':
        question = request.GET.get('question', '').lower()
        response = ""

        if question == "about indian rexine house":
            response = "Indian Rexine House is a premium home decor store offering a wide range of furniture and decor items."
        elif question == "owner contact details":
            response = "You can contact the owner at: Zahir@gmail.com or call +91-9876543210."
        elif "mattress" in question:
            response = "We recommend the Mattress Foam for ₹599. It offers dual comfort with high-density support foam."
        elif "bed" in question:
            response = "We recommend the King Size Wood Bed for ₹2949 is a durable and classic choice."
        elif "pillow" in question:
            response = "We recommend Our Set of Premium Pillows for ₹199 is breathable and hypoallergenic."
        elif "sofa" in question:
            response = " We recommend The Modern L-Shaped Sofa for ₹14999 is a sleek and premium option."
        else:
            response = "Sorry, I couldn't find an answer to your query. Please refine your question."

        return JsonResponse({'response': response})
