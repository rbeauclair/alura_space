from django.urls import path
from galeria.views import index, imagem
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)