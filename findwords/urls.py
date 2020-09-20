from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('documents/', views.document_list, name='document_list'),
    path('interestingwords/', views.words_list, name='words_list'),
    path('upload/', views.upload, name='upload'),
]