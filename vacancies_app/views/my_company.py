from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from vacancies_app.forms import MyCompanyForm, MyVacancyForm, MyProfileForm
from vacancies_app.models import Company, Vacancy, Application


class MyCompanyView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        try:
            company = Company.objects.get(owner=request.user)
        except Company.DoesNotExist:
            return HttpResponseRedirect('letsstart')
        my_company_form = MyCompanyForm(instance=company)
        context = {
            'form': my_company_form,
        }
        return render(request, 'my_company/my_company.html', context=context)

    def post(self, request):
        company = Company.objects.get(owner=request.user)
        my_company_form = MyCompanyForm(request.POST, request.FILES, instance=company)
        if my_company_form.is_valid():
            my_company_save = my_company_form.save(commit=False)
            my_company_save.save()
            return HttpResponseRedirect(reverse_lazy('my_company'))
        return render(request, 'my_company/my_company.html', {'form': my_company_form})


class MyCompanyCreateView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        if len(Company.objects.filter(owner=request.user)) > 0:
            return HttpResponseRedirect('/mycompany/')
        my_company_form = MyCompanyForm()
        context = {
            'form': my_company_form,
        }
        return render(request, 'my_company/my_company_create.html', context=context)

    def post(self, request):
        my_company_form = MyCompanyForm(request.POST, request.FILES)
        if my_company_form.is_valid():
            my_company_create = my_company_form.save(commit=False)
            my_company_create.owner = request.user
            my_company_create.save()
            return HttpResponseRedirect(reverse_lazy('my_company'))
        return render(request, 'my_company/my_company_create.html', {'form': my_company_form})


class MyCompanyLetsstartView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        if len(Company.objects.filter(owner=request.user)) > 0:
            return HttpResponseRedirect(reverse_lazy('my_company'))
        return render(request, 'my_company/my_company_letsstart.html')


class MyCompanyVacanciesView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        vacancies = Vacancy.objects.filter(company__owner=request.user) \
            .annotate(amount_applications=Count('applications'))
        context = {
            'vacancies': vacancies,
        }
        return render(request, 'my_company/my_company_vacancies.html', context=context)


class MyCompanyVacancyCreateView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        my_vacancy_form = MyVacancyForm()

        context = {
            'form': my_vacancy_form,
        }
        return render(request, 'my_company/my_company_vacancy_create.html', context=context)

    def post(self, request):
        my_vacancy_form = MyVacancyForm(request.POST)
        if my_vacancy_form.is_valid():
            my_vacancy_create = my_vacancy_form.save(commit=False)
            my_vacancy_create.company = Company.objects.get(owner=request.user)
            my_vacancy_create.save()
            return HttpResponseRedirect(reverse_lazy('my_company_vacancies'))
        return render(request, 'my_company/my_company_vacancy_create', {'form': my_vacancy_form})


class MyCompanyOneVacancyView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, vacancy_id):
        vacancy = Vacancy.objects.get(id=vacancy_id, company__owner=request.user)
        applications = Application.objects.filter(vacancy__id=vacancy_id)

        my_vacancy_form = MyVacancyForm(instance=vacancy)

        context = {
            'form': my_vacancy_form,
            'vacancy': vacancy.title,
            'applications': applications,
        }
        return render(request, 'my_company/my_company_one_vacancy.html', context=context)

    def post(self, request, vacancy_id):
        vacancy = Vacancy.objects.get(id=vacancy_id)
        my_vacancy_form = MyVacancyForm(request.POST, instance=vacancy)
        if my_vacancy_form.is_valid():
            my_vacancy_save = my_vacancy_form.save(commit=False)
            my_vacancy_save.save()
            return HttpResponseRedirect(reverse_lazy('my_company_vacancies'))
        return render(request, 'my_company/my_company_one_vacancy.html', {'form': my_vacancy_form})


class MyProfileView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        user = User.objects.get(id=request.user.id)
        profile_form = MyProfileForm(instance=user)
        context = {'form': profile_form}
        return render(request, 'my_company/profile.html', context=context)

    def post(self, request):
        user = User.objects.get(id=request.user.id)
        profile_form = MyProfileForm(request.POST, instance=user)
        if profile_form.is_valid():
            my_profile_save = profile_form.save(commit=False)
            my_profile_save.save()
            return HttpResponseRedirect(reverse_lazy('profile'))
        return render(request, 'my_company/profile.html', {'form': profile_form})
