from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    form=UserCreationForm()
    return render(request,'User/Register.html',{'form':form})