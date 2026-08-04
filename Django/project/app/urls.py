from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView
from .views import ProductList,ProductsList,ProductDetailList,ProductCreate,ProductUpdate

urlpatterns = [
    path('home/',views.home,name="home"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('product/',views.addproduct,name="product"),
    path('product/update/<int:id>/',views.updateproduct,name="updateproduct"),
    path('product/delete/<int:id>/',views.deleteProduct,name="deleteproduct"),
    path('product/delete/test/<int:id>/',views.deleteProductTest,name="deleteproducttest"),
    path('user/signup/',views.userSignup,name="userSignup"),
    path('user/signin/',views.usersignin,name="userSigin"),
    path('user/logout/',views.userlogout,name="userlogout"),
    path('productform/',views.productform,name="productform"),
    path('template-home/',TemplateView.as_view(template_name="temptview.html",extra_context={"name":"Apple","color":"red"}),name="template_home"),
    path('template-examp/', ProductList.as_view(), name="template_example"),
    path('product/list/', ProductsList.as_view(), name="product_list"),
    path('product/detail/list/<int:pk>/', ProductDetailList.as_view(), name="product_details"),
    path('product/detail/create/', ProductCreate.as_view(), name="product_create"),
    path('product/detail/update/<int:pk>/', ProductUpdate.as_view(), name="product_update"),
       
]
