from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup_view(request):
    form = UserCreationForm()
    return render (request,'accounts/signup.html',{'form':form})#the third parameter is s dict where the vlaue is the variable we just created
