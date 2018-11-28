from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('index.html', views.homepage, name='homepage'),
    path('contact.html', views.contact, name='contact'),
]

urlpatterns += staticfiles_urlpatterns()

