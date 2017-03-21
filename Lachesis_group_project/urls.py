from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from lachesis import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lachesis/', include('lachesis.urls')),
    # above maps any URLs starting
    # with a lachesis/ to be handled by
    # the lachesis application
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
