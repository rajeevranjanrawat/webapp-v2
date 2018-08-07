
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url, include
from photos.views import photo_list

'''urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^testApp/', include('testApp.urls')),
    url(r'^', include('sites.urls')),

    url(r'crud/', include('crud.urls')),
    url(r'^sites/', include('sites.urls')),
    url(r'^gallery/', photo_list, name='gallery')
]
'''
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^testApp/', include('testApp.urls')),
    url(r'^', include('sites.urls')),

    url(r'crud/', include('crud.urls')),
    url(r'^sites/', include('sites.urls')),
    url(r'^gallery/', photo_list, name='gallery')
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

'''urlpatterns = patterns(”,)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
'''
