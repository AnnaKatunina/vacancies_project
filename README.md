# Django Vacancies project

This application is a web service for searching and posting vacancies,
creating resume, sending job applications.

This application has the following web pages:
- the main page with search
- all vacancies page
- vacancies page by category
- the company's vacancies page
- the vacancy page (with sending a job application functionality in case the user is authenticated)
- job application submission confirmation page
- the search page
- my resume page (creating and editing)
- my company page (creating and editing)
- my company's vacancies page
- my company's vacancy with received applications
- registration, login and logout

The application has been deployed to Heroku
https://jumanji-project.herokuapp.com/

____
## Requirements

- Python 3.7+
- Django 3.1

## Installing

1\. Clone the repository
```
git clone https://github.com/AnnaKatunina/vacancies_project.git
```
2\. Create and activate virtualenv
- for Linux/macOS
```
python -m venv venv
source venv/bin/activate
```
- for Windows
```
python -m venv venv
venv\Scripts\activate
```
3\. Install packages from requirements.txt
```
pip install -r requirements.txt
```
## Usage

Run the application
```
python manage.py runserver
```