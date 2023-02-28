from django.urls import path
from . import views

app_name = 'wordbase'
urlpatterns = [
    path('', views.main, name='main'),
    path('index/', views.index, name='index'),
    path('add_word/', views.add_word, name='add_word'),
    path('run_test/', views.run_test, name='run_test'),
    path('run_test/<int:word_id>/test', views.test, name='test'),
    path('run_test/<int:word_id>/reply', views.reply, name='reply'),
    path('<int:word_id>/edit', views.edit_word, name='edit_word'),
]
