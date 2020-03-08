from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import idea

def idea_list(request):
    all_idea_list = idea.objects.all()
#    template = loader.get_template()
    context = {'all_idea_list': all_idea_list}
    return render(request, 'idea_rank/idea_list.html', context)
#   return HttpResponse(template.render(context, request))

def index(request):
    return render(request,"idea_rank/base.html")