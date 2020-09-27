import os, sys
import nltk
import re

from django.shortcuts import get_object_or_404
from django.contrib.sites.models import get_current_site

from .models import Document, Words, Phrases

#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('names')

def export_text(doc):
    filepath = str(doc)
    filename = os.path.split(filepath)[1]
    extension = os.path.splitext(filename)[1]

    request = None
    if get_current_site(request).domain == 'http://yorkshirelass.pythonanywhere.com/':
        THIS_FOLDER = os.getcwd()
        my_file = os.path.join(THIS_FOLDER, get_current_site(request).domain, filepath)
    else:
        my_file = os.path.join("media", filepath)


    if extension == ".txt":
        with open(my_file, "r", encoding="utf-8") as f:
            data = f.read()
        return data
    else:
        pass


def get_stopwords():

    nltk_stopwords = set(nltk.corpus.stopwords.words("english"))

    new_stopwords = [
        ",",
        ".",
        "'s",
        "us",
        "-",
        "'ve",
        "n't",
        "'re",
        ";",
        "?",
        "'ll",
        "'",
        "''",
        "``",
        "’",
        "'d",
        "one",
        "'m",
        ":",
        "!",
        "$",
        "--",
        "ca",
        "also",
        "even",
        "odd",
        "else",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "%"
    ]
    names = nltk.corpus.names
    male_names = names.words('male.txt')
    female_names = names.words('female.txt')

    all_stopwords = nltk_stopwords.union(new_stopwords, male_names, female_names)

    return all_stopwords


def extract_interesting_words(data, tokenizer):
    """
    Testing word filtering conditions:

    Regex test using https://regex101.com/ - Output: ".\Word-Filtering-Regex-Test.JPG"

    NOT (   in Stopwords    )    AND      contains(r'( \D[^,\.]\D | (\d+/\d+) )') #Contains (non-digit & none of , or .) OR (digits with /)
            <-- (1) -->                   <--------------- (2) ---------------->

    Test 1: word = "better"     # Want True
        (1) = FALSE
        NOT( (1) ) = TRUE
        (2) = TRUE
        NOT( (1) ) AND (2) = TRUE

    Test 2: word = "2,000"     # Want False
        (1) = FALSE
        NOT( (1) ) = TRUE
        (2) = FALSE
        NOT( (1) ) AND (2) = FALSE

    Test 3: word = "9/11"     # Want True
        (1) = FALSE
        NOT( (1) ) = TRUE
        (2) = TRUE
        NOT( (1) ) AND (2) = TRUE

    Test 4: word = "and"     # Want False
        (1) = TRUE
        NOT( (1) ) = FALSE
        (2) = TRUE
        NOT( (1) ) AND (2) = FALSE

    """

    words = nltk.word_tokenize(data)

    all_stopwords = get_stopwords()

    filtered_words = [w for w in words if not(w.lower() in all_stopwords) and re.search(r'(\D[^,\.]\D|(\d+/\d+))', w.lower())]

    fdist = nltk.FreqDist(filtered_words)

    return list(fdist.most_common())


def extract_phrases(data, tokenizer):

    sentences = tokenizer.tokenize(data)

    return sentences


def analyse(doc_uuid):

    doc = get_object_or_404(Document, uuid=doc_uuid)
    filepath = os.path.join("media", os.path.normpath(str(doc.document)))

    data = export_text(filepath)
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    # Get data from file
    if data:
        # Pull out all interesting words from data
        interesting_words = extract_interesting_words(
            data,
            tokenizer
            )
        # If there are interesting words, extract all sentences and match sentences to words
        if interesting_words:
            all_phrases = extract_phrases(
                data,
                tokenizer
                )

            for (w, freq) in interesting_words:
                # Save word and frequency
                word_instance = Words(word=w)
                word_instance.document = doc
                word_instance.occurences = freq
                word_instance.save()

                if all_phrases:
                    for sent in all_phrases:

                        # If Word is not embedded in another word in sentence
                        if re.search( r'(\s|^)+{word}(\s|$|[\.?!;:])+'.format(word=w.lower()), sent.lower() ):
                            # Save sentence
                            sent_instance = Phrases(phrase=sent)
                            sent_instance.word = word_instance
                            sent_instance.save()

        print("Text analysed.")


def get_word_data(new_words, doc_set=Document.objects.all()):
    data = []

    # Get distinct word list
    distinct_words = list(set([x.word for x in new_words]))
    
    for w in distinct_words:
        # Get all occurences of current word
        current_word = [x for x in new_words if x.word == w and x.document in doc_set]

        phrases = list()
        for x in current_word:
            new_phrases = Phrases.objects.filter(word=x)
            [x for x in new_phrases] # cache the queryset
            
            for p in new_phrases:
                sentence = list()
                lower_case_phrase = str(p).lower()
                word_index = lower_case_phrase.find(str(w).lower())
                sentence.append(str(p)[ 0 : word_index ])
                sentence.append(str(w))
                sentence.append(str(p)[ word_index+len(str(w)) : len(str(p)) ])
                phrases.append(sentence)

        distinct_phrases = [tuple(i) for i in phrases]

        data.append({
            'word': w,
            'occurences': sum([x.occurences for x in current_word]),
            'docs': [x.document for x in current_word],
            'phrases': distinct_phrases
        })
    
    try:
        data.sort(key=lambda x: x['occurences'], reverse=True)
    except Exception as e:
        print("Error: Unable to sort data due to exception: {}".format(e))

    return data

