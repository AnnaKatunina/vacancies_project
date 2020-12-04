from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from vacancies_project.settings import MEDIA_COMPANY_IMAGE_DIR, MEDIA_SPECIALITY_IMAGE_DIR


class Specialty(models.Model):
    code = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    picture = models.ImageField(upload_to=MEDIA_SPECIALITY_IMAGE_DIR)

    def __str__(self):
        return f'{self.title}'


class Company(models.Model):
    name = models.CharField('Название компании', max_length=64)
    location = models.CharField('География', max_length=64)
    logo = models.ImageField('Логотип', upload_to=MEDIA_COMPANY_IMAGE_DIR)
    description = models.TextField('Информация о компании')
    employee_count = models.IntegerField('Количество человек в компании')
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Vacancy(models.Model):
    title = models.CharField('Название вакансии', max_length=64)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.CharField('Требуемые навыки', max_length=500)
    description = models.TextField('Описание вакансии')
    salary_min = models.IntegerField('Зарплата от')
    salary_max = models.IntegerField('Зарплата до')
    published_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.title}'


class Application(models.Model):
    written_username = models.CharField('Вас зовут', max_length=64)
    written_phone = models.CharField('Ваш телефон', max_length=14)
    written_cover_letter = models.TextField('Сопроводительное письмо', blank=True)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='applications')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')

    def __str__(self):
        return f'{self.written_username}'


class Resume(models.Model):

    STATUS_CHOICES = (
        ('1', 'Не ищу работу'),
        ('2', 'Рассматриваю предложения'),
        ('3', 'Ищу работу'),
    )

    GRADE_CHOICES = (
        ('1', 'Стажер'),
        ('2', 'Джуниор'),
        ('3', 'Миддл'),
        ('4', 'Синьор'),
        ('5', 'Лид'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField('Имя', max_length=64)
    surname = models.CharField('Фамилия', max_length=64)
    status = models.CharField('Готовность к работе', choices=STATUS_CHOICES, max_length=64)
    salary = models.IntegerField('Вознаграждение')
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    grade = models.CharField('Квалификация', choices=GRADE_CHOICES, max_length=64)
    education = models.TextField('Образование')
    experience = models.TextField('Опыт работы')
    portfolio = models.URLField('Ссылка на портфолио', blank=True)

    def __str__(self):
        return f'{self.name} {self.surname}'
