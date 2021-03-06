# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/All-polls.html'
    # template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/poll_page.html'


class ResultsView(generic.DetailView):
    model = Question
    # template_name = 'polls/results.html'
    template_name = 'polls/results-Modified.html'


class LatestDetailView(generic.ListView):
    context_object_name = 'question_list'
    queryset = Question.objects.order_by('pub_date')
    template_name = 'polls/latest-Polls.html'


def vote(request, question_id):
    # TODO: Complete this question -- partially complete
    question = get_object_or_404(Question, pk=question_id)
    try:  # post['Choice] sent back the Value....
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/poll_page.html', {
            'question': question,
            'error_message': "You forgot to select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
