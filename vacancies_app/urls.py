from django.urls import path

from vacancies_app.views import AllVacanciesView, CompanyView, MainView, VacanciesByCategoryView, VacancyView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('vacancies/', AllVacanciesView.as_view(), name='vacancies'),
    path('vacancies/cat/<category>/', VacanciesByCategoryView.as_view(), name='category'),
    path('companies/<int:id_company>/', CompanyView.as_view(), name='id_company'),
    path('vacancies/<int:id_vacancy>/', VacancyView.as_view(), name='id_vacancy'),
]
