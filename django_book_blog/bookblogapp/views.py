from django.shortcuts import render,redirect
from .models import CreateBook
from .forms import CreateBookForm

# Create your views here.
def home(request):
    context={}
    return render(request,'bookblogapp/index.html',context)

def books(request):
    if request.method == 'POST':
        bookform = CreateBookForm(request.POST)
        if bookform.is_valid():
            book = bookform.save(commit=False)
            book.save()
            return redirect('home')
    else:
        bookform = CreateBookForm()

    return render(request, 'bookblogapp/index.html', {'bookform': bookform})