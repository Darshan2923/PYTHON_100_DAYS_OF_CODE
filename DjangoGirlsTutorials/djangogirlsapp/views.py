from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.

# To display our QuerySet on our blog's post list, we have two things left to do:

# Pass the posts QuerySet to the template context, by changing the render function call. We'll do this now.
# Modify the template to display the posts QuerySet. We'll cover this in a later chapter.

def index(request):
    posts=Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    context={'posts': posts}
    return render(request,'djangogirlsapp/index.html',context)
