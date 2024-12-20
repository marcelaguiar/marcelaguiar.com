from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('blog/', include('blog.urls')),
    path('projects/', include('projects.urls')),
    path('about/', views.about_view, name="about-home"),
    path("ckeditor5/", include('django_ckeditor_5.urls'))
]

if settings.DEBUG:
    # Do not do this in prod
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
