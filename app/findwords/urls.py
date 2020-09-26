from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('documents/', views.document_list, name='all_documents'),
    path('documents/word=(<path:word>)/', views.document_list, name='document_list'),
    path('interestingwords/', views.words_list, name='all_words'),
    path('interestingwords/doc=<uuid:uuid>/', views.words_list, name='words_list'),
    path('upload/', views.upload, name='upload'),
    path('upload/success', views.upload_successful, name='upload_successful'),
]