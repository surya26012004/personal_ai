from django.shortcuts import render
# Create your views here.
import pymysql
def home(request):
    return render(request,"index.html")
def customer(request):
    return render(request,"customer.html")
def signup(request):
    return render(request,"customersignup.html")