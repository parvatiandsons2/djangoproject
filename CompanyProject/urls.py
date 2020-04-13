
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import index, about, services, contactus


admin.site.site_header = "CRM Admin Portal"
admin.site.site_title = "CRM Admin Portal"
admin.site.index_title = "Welcome to CRM Admin Portal"


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('partner/', about, name='partner'),
    path('careers/', about, name='careers'),
    path('terms/', about, name='terms'),
    path('privacy/', about, name='privacy'),
    path('services/', services, name='services'),
    path('services/<slug:service>/', services, name='services'),
    path('support/', include('support.urls')),
    path('customer/', include('customers.urls')),
    path('blogs/', include('blog.urls')),
    path('projects/', include('project.urls')),
    path('announcement/', include('announcement.urls')),
    path('contactus/', contactus, name='contactus'),
    path('startprojects/', index, name='startprojects'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
