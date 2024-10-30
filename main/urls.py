from django.urls import path
from .views import show_main,formulir

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('formulir/', formulir, name='formulir' ),
]