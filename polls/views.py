from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse ,HttpResponseRedirect
from django.urls import reverse
from .models import Question
# Create your views here.

def index(request):
	latest_questions= Question.objects.order_by('-pub_date')[:5]
	return render(request,'polls/index.html',{'latest_questions':latest_questions})


def detail(request, question_id):
	question=Question.objects.get(pk=question_id)
	return render(request, 'polls/detail.html',{'question':question})

def result(request, question_id):
	question= get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/result.html',{'question':question})
	return HttpResponse(result)

def vote(request, question_id):
	question= get_object_or_404(Question,pk=question_id)
	try:
		selected_choice= question.choice_set.get(pk=request.POST['choice'])
	except:
		return render(request, 'polls/detail.html',{'question':question, 'error_message': 'Please select a choice'})

	else:
		selected_choice.vote+=1
		selected_choice.save()	

		return HttpResponseRedirect(reverse('polls:result',args=(question.id,)))