
from django.conf.urls.static import static
from django.urls import path
from .views import *

# from webfront import views

urlpatterns = [
    path('', index, name='home'),
    path('create/', create),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
