from django.shortcuts import render,redirect
from .models import CreateBook

# Create your views here.
def home(request):
    context={}
    return render(request,'bookblogapp/index.html',context)

def books(request):
    if request.method=='POST':
      print(request.POST)
      bookform=CreateBook(request.POST)
      if bookform.is_valid():
         book=bookform.save(commit=False)
         book.save()
      return redirect('home')
    context={'bookform':bookform}
    return render(request,'bookblogapp/index.html',context)
