from django.shortcuts import render


def home(request):
    return render(request, 'findwords/home.html', {})


def document_list(request):
    return render(request, 'findwords/doc_list.html', {})
