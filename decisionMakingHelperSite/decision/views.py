from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question


class IndexView(generic.ListView):
    template_name = 'decision/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-deadline_date')[:20]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'decision/detail.html'


def saveQuestionInDB(request):
    new_question = Question(
        question_text=request.POST['question_text'],
        creation_date=request.POST['creation_date'],
        deadline_date=request.POST['deadline_date']
    )
    new_question.save()
    context = {'question': new_question,}
    return render(request, 'decision/detail.html',context)
