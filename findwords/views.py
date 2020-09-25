from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import DocumentForm
import os
from .utils import analyse


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

    return render(request, page, {'docs': docs, 'word': word, 'total_occur': total})


def words_list(request, uuid=None):
    data = []

    # All Documents
    if uuid==None:
        page = 'findwords/words_multidoc.html'
        all_new_words = Words.objects.all().order_by('word')
        [x for x in all_new_words] # cache the queryset

        if len(all_new_words) == 0:
            page = 'findwords/no_words.html'
        else:
            # Get distinct word list
            distinct_words = list(set([x.word for x in all_new_words]))
            
            for w in distinct_words:
                # Get all occurences of current word
                current_word = [x for x in all_new_words if x.word == w]

                phrases = list()
                for x in current_word:
                    new_phrases = Phrases.objects.filter(word=x)
                    [x for x in new_phrases] # cache the queryset
                    
                    for p in new_phrases:
                        sentence = list()
                        sentence.append(str(p)[ 0 : str(p).find(str(w)) ])
                        sentence.append(str(w))
                        sentence.append(str(p)[ str(p).find(str(w))+len(str(w)) : len(str(p)) ])
                        phrases.append(sentence)

                distinct_phrases = [tuple(i) for i in phrases]

                data.append({
                    'word': w,
                    'occurences': sum([x.occurences for x in current_word]),
                    'docs': [x.document for x in current_word],
                    'phrases': distinct_phrases
                })
        
    # Single Document
    elif not(uuid==None):
        page = 'findwords/words_sgldoc.html'
        doc = get_object_or_404(Document, uuid=uuid)
        new_words = Words.objects.filter(document=doc)
        [w for w in new_words] # cache the queryset

        for w in new_words:
            data.append({
                'word': w,
                'occurences': w.occurences,
                'doc': doc,
                'phrases': [
                    (
                        str(p)[ 0 : str(p).find(str(w)) ],
                        str(w),
                        str(p)[ str(p).find(str(w))+len(str(w)) : len(str(p)) ]
                    ) for p in Phrases.objects.filter(word=w)
                    ]
            })

    try:
        data.sort(key=lambda x: x['occurences'], reverse=True)
    except Exception as e:
        print("Error: Unable to sort data due to exception: {}".format(e))

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
                analyse(doc_instance.uuid)
            return redirect('upload_successful')
    else:
        form = DocumentForm()
    return render(request, 'findwords/upload.html', {'form': form})


def upload_successful(request):
    return render(request, 'findwords/upload-successful.html')
