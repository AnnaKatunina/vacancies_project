from django.urls import path

from vacancies_app.views import AllVacanciesView, CompanyView, MainView, VacanciesByCategoryView, VacancyView, \
    SentVacancyView, MyCompanyView, MyCompanyVacanciesView, MyCompanyOneVacancyView, MyLoginView, RegisterView, \
    MyLogoutView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('vacancies/', AllVacanciesView.as_view(), name='vacancies'),
    path('vacancies/cat/<category>/', VacanciesByCategoryView.as_view(), name='category'),
    path('companies/<int:id_company>/', CompanyView.as_view(), name='id_company'),
    path('vacancies/<int:id_vacancy>/', VacancyView.as_view(), name='id_vacancy'),
    path('vacancies/<int:vacancy_id>/send/', SentVacancyView.as_view(), name='id_vacancy_send'),
    path('mycompany/', MyCompanyView.as_view(), name='my_company'),
    path('mycompany/vacancies/', MyCompanyVacanciesView.as_view(), name='my_company_vacancies'),
    path('mycompany/vacancies/<int:vacancy_id>', MyCompanyOneVacancyView.as_view(), name='my_company_one_vacancy'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
]
