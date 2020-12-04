from django.urls import path

from vacancies_app.views.my_company import MyCompanyVacanciesView, MyCompanyLetsstartView, MyCompanyCreateView, \
    MyCompanyView, MyCompanyOneVacancyView, MyCompanyVacancyCreateView, MyProfileView
from vacancies_app.views.my_resume import MyResumeView, MyResumeStartView, MyResumeCreateView
from vacancies_app.views.public import MainView, AllVacanciesView, VacanciesByCategoryView, CompanyView, VacancyView, \
    SentVacancyView, MyLoginView, RegisterView, MyLogoutView, SearchView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('vacancies/', AllVacanciesView.as_view(), name='vacancies'),
    path('vacancies/cat/<category>/', VacanciesByCategoryView.as_view(), name='category'),
    path('companies/<int:id_company>/', CompanyView.as_view(), name='id_company'),
    path('vacancies/<int:id_vacancy>/', VacancyView.as_view(), name='id_vacancy'),
    path('vacancies/<int:vacancy_id>/send/', SentVacancyView.as_view(), name='id_vacancy_send'),
    path('mycompany/', MyCompanyView.as_view(), name='my_company'),
    path('mycompany/create/', MyCompanyCreateView.as_view(), name='my_company_create'),
    path('mycompany/letsstart/', MyCompanyLetsstartView.as_view(), name='my_company_letsstart'),
    path('mycompany/vacancies/', MyCompanyVacanciesView.as_view(), name='my_company_vacancies'),
    path('mycompany/vacancies/<int:vacancy_id>/', MyCompanyOneVacancyView.as_view(), name='my_company_one_vacancy'),
    path('mycompany/vacancies/create/', MyCompanyVacancyCreateView.as_view(), name='my_company_vacancy_create'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('profile/', MyProfileView.as_view(), name='profile'),
    path('myresume/', MyResumeView.as_view(), name='my_resume'),
    path('myresume/create/', MyResumeCreateView.as_view(), name='my_resume_create'),
    path('myresume/start/', MyResumeStartView.as_view(), name='my_resume_start'),
    path('search/', SearchView.as_view(), name='search'),
]
