from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.
def index(request):
    return render(request,'test/index.html')
def signup(request):
    if(request.method=='POST'):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User(username=username, email=email, password=password)
        user.save()
    return render(request, 'test/index.html')
