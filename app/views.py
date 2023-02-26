from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from app. forms import *
from django.http import HttpResponse


# class cbvtemplate(TemplateView):
#     template_name='cbvtemplate.html'

class CbvContext(TemplateView):
    template_name='CbvContext.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='ASHU'
        context['age']=3
        return context


class formtemplate(TemplateView):
    template_name='cbvform.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['form']=forms.student()
        return  context

    def post(self,request):
       form_data=forms.student(request.POST)
       if form_data.is_valid():
        print(form_data.cleaned_data)
        return HttpResponse('form is valid')