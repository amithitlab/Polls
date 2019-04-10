from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.

def index(request):
	latest_questions= Question.objects.order_by('-pub_date')[:5]
	#template = loader.get_template('polls/index.html')
	#context=RequestContext(request, {'latest_questions': latest_questions})
	#return HttpResponse(template.render(context.flatten()))
	return render(request,'polls/index.html',{'latest_questions':latest_questions})


def detail(request, question_id):
	detail = 'This is the detail of the question: '+question_id
	return HttpResponse(detail)

def result(request, question_id):
	result = 'This is the result of the question: '+question_id
	return HttpResponse(result)

def vote(request, question_id):
	vote="Vote on question: "+question_id
	return HttpResponse(vote)