from django.contrib import admin
from django.urls import path
from . import views

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
]
