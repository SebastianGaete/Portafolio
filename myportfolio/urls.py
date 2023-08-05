from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('detail_project/<int:id>', detail_project, name='detail_project'),
    path('contact/', contact, name='contact'),
    path('comentario/', comentarios, name='comentario')
]