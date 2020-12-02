from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Count
from django.http import Http404, HttpResponseNotFound, HttpResponseServerError, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from vacancies_app.forms import RegisterUserForm, LoginForm, ApplicationForm
from vacancies_app.models import Specialty, Company, Vacancy


class MainView(View):

    def get(self, request):
        specialties = Specialty.objects.all().annotate(amount_vacancies=Count('vacancies'))
        companies = Company.objects.all().annotate(amount_vacancies=Count('vacancies'))

        context = {
            'list_of_categories': specialties,
            'list_of_companies': companies,
        }
        return render(request, 'index.html', context=context)


class AllVacanciesView(View):

    def get(self, request):
        vacancies = Vacancy.objects.select_related('company').all()
        context = {'list_of_vacancies': vacancies}
        return render(request, 'vacancies.html', context=context)


class VacanciesByCategoryView(View):

    def get(self, request, category):
        try:
            category_title = Specialty.objects.get(code=category).title
        except Specialty.DoesNotExist:
            raise Http404
        vacancies = Vacancy.objects.select_related('company').filter(specialty__code=category)
        context = {
            'list_of_vacancies': vacancies,
            'category': category_title,
            }
        return render(request, 'vacancies_category.html', context=context)


class CompanyView(View):

    def get(self, request, id_company):
        try:
            company = Company.objects.get(id=id_company)
        except Company.DoesNotExist:
            raise Http404
        vacancies = Vacancy.objects.filter(company__id=id_company)
        context = {
            'company': company,
            'list_of_vacancies': vacancies,
        }
        return render(request, 'company.html', context=context)


class VacancyView(View):

    def get(self, request, id_vacancy):
        try:
            vacancy = Vacancy.objects.get(id=id_vacancy)
        except Vacancy.DoesNotExist:
            raise Http404
        application_form = ApplicationForm()
        context = {
            'vacancy': vacancy,
            'form': application_form,
        }

        return render(request, 'vacancy.html', context=context)

    def post(self, request, id_vacancy):
        application_form = ApplicationForm(request.POST)
        if application_form.is_valid():
            application = application_form.save(commit=False)
            application.user = request.user
            #vacancy = Vacancy.objects.get(id=id_vacancy)
            application.vacancy = request.vacancy
            application.save()
            return HttpResponseRedirect('send')


class SentVacancyView(View):

    def get(self, request, vacancy_id):
        return render(request, 'sent_vacancy.html')


class MyCompanyView(View):

    def get(self, request):
        return render(request, 'my_company.html')


class MyCompanyVacanciesView(View):

    def get(self, request):
        return render(request, 'my_company_vacancies.html')


class MyCompanyOneVacancyView(View):

    def get(self, request, vacancy_id):
        return render(request, 'my_company_one_vacancy.html')


class MyLoginView(LoginView):
    form_class = LoginForm
    redirect_authenticated_user = True
    template_name = 'login.html'


class RegisterView(CreateView):
    form_class = RegisterUserForm
    success_url = '/login/'
    template_name = 'register.html'


class MyLogoutView(LogoutView):
    next_page = '/login/'


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ошибка 404')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка 500')
