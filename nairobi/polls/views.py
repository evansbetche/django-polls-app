from multiprocessing import context
from django.shortcuts import render

# Create your views here.
from django.http import Http404, HttpResponse
from django.template import loader

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #1. Using a short cut: render()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

    #2. Using a common way to load a template
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    def detail(request, question_id):
        # try:
        #     question = Question.objects.get(pk=question_id)
        # except Question.DoesNotExist:
        #     raise Http404("Question does not exist")
        # return render(request, 'polls/detail.html', {'question': question})

        #A shortcut: get_object-or_404()
        question = get_object_or_404(Question, pk = question_id)
        return render(request, 'polls/detail.html', {'question': question})
        




# def  index(request):
#     return HttpResponse("Hello, Welcome to my polls website.")

# def detail(request, question_id):
#     return  HttpResponse("You're looking at question %s." % question_id)

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

