import debug_toolbar
from django.contrib import admin
from django.urls import include, path

from vacancies_app.views import custom_handler404, custom_handler500

urlpatterns = [
    path('', include('vacancies_app.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
]

handler404 = custom_handler404
handler500 = custom_handler500
