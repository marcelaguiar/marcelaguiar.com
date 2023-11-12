from django.conf import settings
from django.urls import path
from .views import main

urlpatterns = [
    path('home', main),
    path('', main),
]

if settings.DEBUG:
    # Do not do this in prod
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)