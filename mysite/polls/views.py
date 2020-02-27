from django.shortcuts import render
from django.http import Http404

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(f"You're looking at question {question_id}")

def results(request, question_id):
    return HttpResponse(f"You're looking at the result of question {question_id}")

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")