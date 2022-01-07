from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from pollapp.models import Question

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-publish')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'pollapp/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'pollapp/detail.html', {'question': question})


def results(request, question_id):
    response = 'You are looking at the results of the questions %s.'
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
