from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from datetime import date
from .models import Product

from django.urls import reverse_lazy


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


def productfilter(request):
    if request.method == "POST":
        searchtext=request.POST['search']
        prd=Product.objects.filter(product_name__icontains=searchtext)
        return render(request,"filter.html",{"product":prd})
    prd=Product.objects.all()
    return render(request,"filter.html",{"product":prd})


from django.contrib.auth.models import User
def userSignup(request):
    if request.method =="POST":
        uname=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')

        if password != confirm_password:
            print("Password Mismatch")
            return redirect('userSignup')

        usr=User.objects.create_user(
            username=uname,
            email=email,
            password=password
        )
        print(usr,"User Created Successfully")
    return render (request,"signup.html")

from django.contrib.auth import authenticate,login
def usersignin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(
            username=username,
            password=password
        )
        if user:
            login(request,user)
            return redirect('home')
        else:
            print("Invalid Credentials")
    return render (request,"signin.html")

from django.contrib.auth import logout
def userlogout(request):
    logout(request);
    return redirect('userSigin')

from .forms import ProductForm
def productform(request):
    if request.method=="POST":
        print("Product from Form")
        prdtform=ProductForm(request.POST)
        if prdtform.is_valid():
            prdtform.save()
            print("Success")
            return redirect("productform")
        else:
            print("Success")
            prdtform=ProductForm()
    prdt=Product.objects.all()
    return render(request,"form/prodtform.html",{"ProductForm":ProductForm,"prdt":prdt})

from django.views.generic import TemplateView,ListView,DetailView
class ProductList(TemplateView):
    template_name="class/tempview.html"
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['name']="orange"
        context['color']="RedishOrange"
        context['price']="210.2"
        return context

class ProductsList(ListView):
    model=Product
    template_name="class/productlist.html"
    context_object_name='product'

    # def get_queryset(self):
    #     return Product.objects.filter(rating)

class ProductDetailList(DetailView):
    model=Product
    template_name="class/productdetaillist.html"
    context_object_name='product'

from django.views.generic.edit  import CreateView,UpdateView,DeleteView

class ProductCreate(CreateView):
    model=Product
    template_name="class/createproduct.html"
    fields=['product_name','price','description','rating']
    success_url=reverse_lazy('product_list')

class ProductUpdate(UpdateView):
    model=Product
    template_name="class/updateproduct.html"
    fields=['product_name','price','description','rating']
    success_url=reverse_lazy('product_list')


class ProductDelete(DeleteView):
    model = Product
    template_name = "class/deleteproduct.html"
    success_url = reverse_lazy("product_list")

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
class ProductApiView(APIView):
    def get(self,request):
        prd=Product.objects.all()
        serializer=ProductSerializer(prd,many=True)
        return Response(serializer.data)
    
    def post(self,request):
       
        serializer=ProductSerializer(data=request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def put(self,request,pk):
        # prd=Product.objects.get(id=pk) 
        prd=get_object_or_404(Product,id=pk)
        serializer=ProductSerializer(prd,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    def patch(self,request,pk):
        # prd=Product.objects.get(id=pk) 
        prd=get_object_or_404(Product,id=pk)
        serializer=ProductSerializer(prd,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def delete(self,request,pk):
        prd=get_object_or_404(Product,id=pk)
        # prd=Product.objects.get(id=pk) 
        prd.delete()
        return Response({"message":"Product Deleted Successfully"})
