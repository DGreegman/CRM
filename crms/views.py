from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()

    total_customers = customers.count()
    total_order = orders.count()
    pending = orders.filter(status='Pending').count()
    delivered = orders.filter(status='Delivered').count()
    context = {
        'customers': customers,
        'orders' : orders, 
        'total_customers' : total_customers,
        'total_order': total_order,
        'delivered': delivered,
        'pending': pending
    }
    return render(request, 'crms/dashboard.html', context)


def products(request):
    products = Product.objects.all()
    return render(request, 'crms/products.html', {'products':products})


def customer(request):
    return render(request, 'crms/customer.html')