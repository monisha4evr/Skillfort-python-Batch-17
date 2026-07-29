from django.shortcuts import render,redirect,get_object_or_404
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

def updateproduct(request,id):
    pt=Product.objects.get(id=id)
    if request.method == "POST":
        pt.product_name=request.POST.get('product_name')
        pt.price=request.POST.get('price')
        pt.description=request.POST.get('description')
        pt.rating=request.POST.get('rating')
        pt.save()
        return redirect("product")
    return render(request,"update.html")

def deleteProduct(request,id):
    pt=Product.objects.get(id=id)
    pt.delete()    
    return redirect("product")

def deleteProductTest(request,id=id):
    pt=get_object_or_404(Product,id=id)
    pt.delete()
    return redirect("product")