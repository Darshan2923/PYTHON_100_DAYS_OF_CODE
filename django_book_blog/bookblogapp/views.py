from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    context={}
    return render(request,'bookblogapp/index.html',context)

def books(request):
    context={}
    return render(request,'bookblogapp/index.html',context)
