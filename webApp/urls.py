"""webApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url, include
from photos.views import photo_list

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^testApp/', include('testApp.urls')),
    url(r'^', include('sites.urls')),

    url(r'crud/', include('crud.urls')),
    url(r'^sites/', include('sites.urls')),
    url(r'^gallery/', photo_list, name='gallery')
]
'''urlpatterns = patterns(”,)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)'''
'''if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
'''
if not settings.DEBUG:
    urlpatterns += patterns”,
    (r’^static/(.*)$’, ‘django.views.static.serve’, {‘document_root’: settings.STATIC_ROOT}),)
