from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Question

# Create your views here.
def index (request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render (request,'enquete/index.html',context)


def vote (request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except KeyError:
        return render (request, 'enquete/vote.html', {
            'question':question,
            'error message':'você não selecionou um resposta ',
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('enquete:results', args= (question_id,)))

        

def results (request, question_id):
    question = Question(pk =question_id)
    return render (request, 'enquete/results.html',{'question':question})

