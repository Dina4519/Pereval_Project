from django.contrib import admin
from django.urls import path, include
from pereval.views import *

from django.views.generic import TemplateView

from rest_framework import routers
from pereval import viewsets

from .yasg import urlpatterns as doc_urls

router = routers.SimpleRouter()
router.register(r'submitData', PerevalViewset, basename='pereval')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('swagger-ui/', TemplateView.as_view(
    template_name='swagger-ui.html',
    extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('pages/', include('django.contrib.flatpages.urls')),

    path('pereval/', include('pereval.urls')),
    path('', include(router.urls)),
   # path('ckeditor/', include('ckeditor_uploader.urls')),
   #  path('', include('protect.urls')),
   #  path('sign/', include('sign.urls')),
   #  path('accounts/', include('allauth.urls')),
]

urlpatterns += doc_urls
