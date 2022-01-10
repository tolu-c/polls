from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from pollapp.models import Question, Choice

# Create your views here.


# def index(request):
#     latest_question_list = Question.objects.order_by('-publish')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'pollapp/index.html', context)

class IndexView(generic.ListView):
    template_name = 'pollapp/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        return Question.objects.order_by('-publish')[:5]


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'pollapp/detail.html', {'question': question})

class DetailView(generic.DetailView):
    model = Question
    template_name = 'pollapp/detail.html'


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'pollapp/results.html', {'question': question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'pollapp/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'pollapp/detail.html', {
            'question': question,
            'error_message': 'You didn\'t select a choice'
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('pollapp:results', args=(question.id)))
