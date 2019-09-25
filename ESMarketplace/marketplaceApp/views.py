from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choices, Question


class IndexView(generic.ListView):
    template_name = 'marketplaceApp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions, not including future questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'marketplaceApp/details.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'marketplaceApp/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choices_set.get(pk=request.POST['choice'])
    except (KeyError, Choices.DoesNotExist):
        return render(request, 'marketplaceApp/details.html',
                      {'question': question, 'error_message': "You didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        print(question_id)
        return HttpResponseRedirect(reverse('marketplaceApp:results', kwargs={'pk': question_id}))




