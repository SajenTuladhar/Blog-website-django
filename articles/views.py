from django.shortcuts import render

# Create your views here.
def article_list(request):
    return render(request,'articles/article_list.html') #django looks in templates and finds article folder 