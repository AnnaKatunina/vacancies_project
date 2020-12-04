from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from vacancies_app.forms import MyResumeForm
from vacancies_app.models import Resume


class MyResumeView(View):

    def get(self, request):
        if request.user.is_authenticated:
            try:
                resume = Resume.objects.get(user=request.user)
            except Resume.DoesNotExist:
                return HttpResponseRedirect('start')
            my_resume_form = MyResumeForm(instance=resume)
            context = {'form': my_resume_form}
            return render(request, 'my_resume/resume_edit.html', context=context)
        else:
            return HttpResponseRedirect('/login/')

    def post(self, request):
        resume = Resume.objects.get(user=request.user)
        my_resume_form = MyResumeForm(request.POST, instance=resume)
        if my_resume_form.is_valid():
            my_resume_save = my_resume_form.save(commit=False)
            my_resume_save.save()
            return HttpResponseRedirect('/myresume/')
        return render(request, 'my_resume/resume_edit.html', {'form': my_resume_form})


class MyResumeCreateView(View):

    def get(self, request):
        if request.user.is_authenticated:
            if len(Resume.objects.filter(user=request.user)) > 0:
                return HttpResponseRedirect('/myresume/')
            my_resume_form = MyResumeForm()
            context = {'form': my_resume_form}
            return render(request, 'my_resume/resume_create.html', context=context)
        else:
            return HttpResponseRedirect('/login/')

    def post(self, request):
        my_resume_form = MyResumeForm(request.POST)
        if my_resume_form.is_valid():
            my_resume_create = my_resume_form.save(commit=False)
            my_resume_create.user = request.user
            my_resume_create.save()
            return HttpResponseRedirect('/myresume/')
        return render(request, 'my_resume/resume_create.html', {'form': my_resume_form})


class MyResumeStartView(View):

    def get(self, request):
        if request.user.is_authenticated:
            if len(Resume.objects.filter(user=request.user)) > 0:
                return HttpResponseRedirect('/myresume/')
            return render(request, 'my_resume/resume_start.html')
        else:
            return HttpResponseRedirect('/login/')
