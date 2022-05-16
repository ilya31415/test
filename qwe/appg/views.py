from django.shortcuts import render

# Create your views here.


def gen(request):
    template = 'articles/qwee.html'

    context = {'object_list': 'asd'}


    return render(request, template, context)
