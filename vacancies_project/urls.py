import debug_toolbar
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from vacancies_app.views.public import custom_handler404, custom_handler500
from vacancies_project import settings

urlpatterns = [
    path('', include('vacancies_app.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
]

handler404 = custom_handler404
handler500 = custom_handler500

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
