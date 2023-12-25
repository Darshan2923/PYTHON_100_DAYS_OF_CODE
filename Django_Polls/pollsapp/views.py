from django.shortcuts import render,HttpResponse,redirect
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
# Create your views here.
from .models import *


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('pollsapp/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'pollsapp/index.html', context)

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'pollsapp/detail.html', {'question': question})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'pollsapp/detail.html', {'question': question})

# There’s also a get_list_or_404() function, which works just as get_object_or_404() – except using filter() instead of get(). It raises Http404 if the list is empty.

def results(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'pollsapp/results.html',{'question':question})

def vote(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        # Redisplay the question voting form.
        context={'question':question,'error_message':"You didn't select a choice"}
        return render(request,'pollsapp/detail.html',context)
    else:
        selected_choice.votes+=1
        selected_choice.save()
    return redirect('pollsapp:results', question_id=question.id)