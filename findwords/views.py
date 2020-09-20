from django.shortcuts import render
from .models import Document


def home(request):
    return render(request, 'findwords/home.html', {})


def document_list(request):
    docs = Document.objects.filter().order_by('upload_time')
    return render(request, 'findwords/doc_list.html', {'docs': docs})


def words_list(request, uuid):
    doc = Document.objects.filter().order_by('upload_time')
    words = []
    phrases = []
    return render(request, 'findwords/words_list.html', {'doc': doc, 'words': words, 'phrases': phrases})


def upload(request):
    pass
