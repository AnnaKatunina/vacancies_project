from datetime import datetime
import locale

from django.http import Http404, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from django.views import View

from vacancies_app.models import Specialty, Company, Vacancy

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


class MainView(View):

    def get(self, request):
        specialties = Specialty.objects.all()
        companies = Company.objects.all()

        list_of_categories = []
        for specialty in specialties:
            specialty_dict = {
                'code': specialty.code,
                'title': specialty.title,
                'picture': specialty.picture,
                'amount_vacancies': Vacancy.objects.filter(specialty__code=specialty.code).count(),
            }
            list_of_categories.append(specialty_dict)

        list_of_companies = []
        for company in companies:
            company_dict = {
                'id': company.id,
                'name': company.name,
                'logo': company.logo,
                'amount_vacancies': Vacancy.objects.filter(company__name=company.name).count(),
            }
            list_of_companies.append(company_dict)

        context = {
            'list_of_categories': list_of_categories,
            'list_of_companies': list_of_companies,
        }
        return render(request, 'index.html', context=context)


class AllVacanciesView(View):

    def get(self, request):
        vacancies = Vacancy.objects.select_related('company').all()
        list_of_vacancies = []
        for vacancy in vacancies:
            vacancy_skills = vacancy.skills.replace(', ', ' • ')
            published_date = datetime.strftime(vacancy.published_at, '%d %B')
            salary_min = '{:,}'.format(vacancy.salary_min).replace(',', ' ')
            salary_max = '{:,}'.format(vacancy.salary_max).replace(',', ' ')
            vacancy_dict = {
                'id': vacancy.pk,
                'title': vacancy.title,
                'company_logo': vacancy.company.logo,
                'company_id': vacancy.company.id,
                'vacancy_skills': vacancy_skills,
                'salary_min': salary_min,
                'salary_max': salary_max,
                'published_date': published_date,
            }
            list_of_vacancies.append(vacancy_dict)

        context = {'list_of_vacancies': list_of_vacancies}

        return render(request, 'vacancies.html', context=context)


class VacanciesByCategoryView(View):

    def get(self, request, category):
        try:
            Specialty.objects.get(code=category)
        except Specialty.DoesNotExist:
            raise Http404
        vacancies = Vacancy.objects.select_related('company').filter(specialty__code=category)
        category_title = Specialty.objects.get(code=category).title
        list_of_vacancies = []
        for vacancy in vacancies:
            vacancy_skills = vacancy.skills.replace(', ', ' • ')
            published_date = datetime.strftime(vacancy.published_at, '%d %B')
            salary_min = '{:,}'.format(vacancy.salary_min).replace(',', ' ')
            salary_max = '{:,}'.format(vacancy.salary_max).replace(',', ' ')
            vacancy_dict = {
                'id': vacancy.pk,
                'title': vacancy.title,
                'company_logo': vacancy.company.logo,
                'company_id': vacancy.company.id,
                'vacancy_skills': vacancy_skills,
                'salary_min': salary_min,
                'salary_max': salary_max,
                'published_date': published_date,
            }
            list_of_vacancies.append(vacancy_dict)

        context = {
            'list_of_vacancies': list_of_vacancies,
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
        list_of_vacancies = []
        for vacancy in vacancies:
            vacancy_skills = vacancy.skills.replace(', ', ' • ')
            published_date = datetime.strftime(vacancy.published_at, '%d %B')
            salary_min = '{:,}'.format(vacancy.salary_min).replace(',', ' ')
            salary_max = '{:,}'.format(vacancy.salary_max).replace(',', ' ')
            vacancy_dict = {
                'id': vacancy.pk,
                'title': vacancy.title,
                'vacancy_skills': vacancy_skills,
                'salary_min': salary_min,
                'salary_max': salary_max,
                'published_date': published_date,
                }
            list_of_vacancies.append(vacancy_dict)

        context = {
            'company': company,
            'list_of_vacancies': list_of_vacancies,
        }
        return render(request, 'company.html', context=context)


class VacancyView(View):

    def get(self, request, id_vacancy):
        try:
            vacancy = Vacancy.objects.get(id=id_vacancy)
        except Vacancy.DoesNotExist:
            raise Http404
        vacancy_skills = vacancy.skills.replace(', ', ' • ')
        salary_min = '{:,}'.format(vacancy.salary_min).replace(',', ' ')
        salary_max = '{:,}'.format(vacancy.salary_max).replace(',', ' ')

        context = {
            'vacancy': vacancy,
            'vacancy_skills': vacancy_skills,
            'salary_min': salary_min,
            'salary_max': salary_max,
        }
        return render(request, 'vacancy.html', context=context)


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ошибка 404')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка 500')
