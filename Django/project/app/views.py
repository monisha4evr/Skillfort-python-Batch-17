from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from .models import Product

# Create your views here.
def home(request):
    return render(request,"home.html")

def contact(request):
    return HttpResponse("Hello World")

def about(request):
    info={
        'name':'apple',
        "color":"Green",
        "price":120,
        "origin":['kashmir','chennai'],
        "Reached":date(2026,7,23)
    }
    return render(request,"about.html",info)

def addproduct(request):
    if request.method=="POST":
        product_name=request.POST.get('product_name')
        price=request.POST.get('price')
        descp=request.POST.get('description')
        rating=request.POST.get('rating')
        prd=Product.objects.create(
            product_name=product_name,
            price=price,
            description=descp,
            rating=rating
        )
        print(prd)
    prd_details=Product.objects.all()
    return render(request,"product.html",{"product":prd_details})