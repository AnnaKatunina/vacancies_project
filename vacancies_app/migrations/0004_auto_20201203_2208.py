# Generated by Django 3.1.3 on 2020-12-03 22:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vacancies_app', '0003_auto_20201201_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='written_cover_letter',
            field=models.TextField(blank=True, verbose_name='Сопроводительное письмо'),
        ),
        migrations.AlterField(
            model_name='application',
            name='written_phone',
            field=models.CharField(max_length=14, verbose_name='Ваш телефон'),
        ),
        migrations.AlterField(
            model_name='application',
            name='written_username',
            field=models.CharField(max_length=64, verbose_name='Вас зовут'),
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(verbose_name='Информация о компании'),
        ),
        migrations.AlterField(
            model_name='company',
            name='employee_count',
            field=models.IntegerField(verbose_name='Количество человек в компании'),
        ),
        migrations.AlterField(
            model_name='company',
            name='location',
            field=models.CharField(max_length=64, verbose_name='География'),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(upload_to='company_images', verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Название компании'),
        ),
        migrations.AlterField(
            model_name='company',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=models.TextField(verbose_name='Описание вакансии'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='published_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary_max',
            field=models.IntegerField(verbose_name='Зарплата до'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary_min',
            field=models.IntegerField(verbose_name='Зарплата от'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='skills',
            field=models.CharField(max_length=500, verbose_name='Требуемые навыки'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='title',
            field=models.CharField(max_length=64, verbose_name='Название вакансии'),
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Имя')),
                ('surname', models.CharField(max_length=64, verbose_name='Фамилия')),
                ('status', models.CharField(choices=[('1', 'Не ищу работу'), ('2', 'Рассматриваю предложения'), ('3', 'Ищу работу')], max_length=64, verbose_name='Готовность к работе')),
                ('salary', models.IntegerField(verbose_name='Вознаграждение')),
                ('grade', models.CharField(choices=[('1', 'Стажер'), ('2', 'Джуниор'), ('3', 'Ищу работу'), ('4', 'Синьор'), ('5', 'Лид')], max_length=64, verbose_name='Квалификация')),
                ('education', models.TextField(verbose_name='Образование')),
                ('experience', models.TextField(verbose_name='Опыт работы')),
                ('portfolio', models.URLField(verbose_name='Ссылка на портфолио')),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancies_app.specialty')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
