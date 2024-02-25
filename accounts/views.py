from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid(): # checks if the value inserted by user is correct and meets requirement or not
         form.save() #creates a new user for us
         #log the user in
         return redirect('articles:list') #name of the app is article tha we defined and the list is the name of the url that we defined as well
    else:
        form = UserCreationForm()
    return render (request,'accounts/signup.html',{'form':form})#the third parameter is s dict where the vlaue is the variable we just created
