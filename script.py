import os
import django
from datetime import datetime

from vacancies_app.data import jobs, companies, specialties


os.environ["DJANGO_SETTINGS_MODULE"] = 'vacancies_project.settings'
django.setup()


from vacancies_app.models import Company, Specialty, Vacancy


if __name__ == '__main__':

    for specialty in specialties:
        Specialty.objects.create(
            code=specialty['code'],
            title=specialty['title'],
            picture=f'https://raw.githubusercontent.com/kushedow/flask-html/master'
                    f'/Django%20Project%202/specialties/specty_{specialty["code"]}.png',
        )

    for company in companies:
        Company.objects.create(
            name=company['title'],
            location=company['location'],
            logo=f'https://raw.githubusercontent.com/kushedow/flask-html/master/Django%20Project%202/'
                 f'static/{company["logo"]}',
            description=company['description'],
            employee_count=int(company['employee_count']),
        )

    for vacancy in jobs:
        Vacancy.objects.create(
            title=vacancy['title'],
            specialty=Specialty.objects.get(code=vacancy['specialty']),
            company=Company.objects.get(id=int(vacancy['company'])),
            skills=vacancy['skills'],
            description=vacancy['description'],
            salary_min=int(vacancy['salary_from']),
            salary_max=int(vacancy['salary_to']),
            published_at=datetime.strptime(vacancy['posted'], '%Y-%m-%d'),
        )
