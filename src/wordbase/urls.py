from django.urls import path
from . import views

app_name = 'wordbase'
urlpatterns = [
    path('', views.main, name='main'),
    path('index/', views.index, name='index'),
    path('add_word/', views.add_word, name='add_word'),
    path('int:word_id/test', views.test, name='test'),
    path('int:word_id/edit', views.edit_word, name='edit_word'),
]
