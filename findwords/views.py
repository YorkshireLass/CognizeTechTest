from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import DocumentForm
import os
from .utils import analyse, get_word_data


def home(request):
    return render(request, 'findwords/home.html', {})


def document_list(request, word=None):

    # All Words
    if word==None:
        total = 0
        docs = Document.objects.all().order_by('upload_time')
        if len(docs) == 0:
            page = 'findwords/no_docs.html'
        else:
            page = 'findwords/doc_list.html'
    # Specific Word provided
    else:
        all_words = Words.objects.all().order_by('word')
        docs = [{'doc': x.document, 'occurences': x.occurences} for x in all_words if x.word == word]
        docs.sort(key=lambda x: x['occurences'], reverse=True)
        total = sum([x['occurences'] for x in docs])
        page = 'findwords/doc_list_specificword.html'

    return render(request, page, {'docs': docs, 'word': word.title(), 'total_occur': total})


def words_list(request, uuid=None):
    data = []

    # All Documents
    if uuid==None:
        page = 'findwords/words_multidoc.html'
        all_new_words = Words.objects.all().order_by('word')

        if len(all_new_words) == 0:
            page = 'findwords/no_words.html'
        else:
            data = get_word_data(all_new_words)

    # Single Document
    elif not(uuid==None):
        page = 'findwords/words_sgldoc.html'
        doc = get_object_or_404(Document, uuid=uuid)
        new_words = Words.objects.filter(document=doc)
        data = get_word_data(new_words, doc_set=[doc])

    return render(request, page, {'data': data})


def upload(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        files = request.FILES.getlist('document')
        if form.is_valid():
            for f in files:
                doc_instance = Document(document=f)
                filepath = str(f)
                filename = os.path.split(filepath)[1]
                doc_instance.title = os.path.splitext(filename)[0]
                doc_instance.save()
                print("Uploaded document: ", doc_instance, " - ", doc_instance.uuid)

                current_site = request.get_host()
                analyse(doc_instance.uuid, current_site)

            return redirect('upload_successful')
    else:
        form = DocumentForm()
    return render(request, 'findwords/upload.html', {'form': form})


def upload_successful(request):
    return render(request, 'findwords/upload-successful.html')
