from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from simplemooc.core.views import contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('simplemooc.core.urls')),
    path('cursos/', include('simplemooc.courses.urls')),
    path('contato/', contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)