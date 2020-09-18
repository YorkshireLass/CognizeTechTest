from django.shortcuts import render
from .models import Document


def home(request):
    return render(request, 'findwords/home.html', {})


def document_list(request):
    docs = Document.objects.filter().order_by('upload_time')
    return render(request, 'findwords/doc_list.html', {'docs': docs})
