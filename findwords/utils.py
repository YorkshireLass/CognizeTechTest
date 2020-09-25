import os, sys
import nltk

from django.shortcuts import get_object_or_404

from .models import Document, Words, Phrases

#nltk.download('punkt')
#nltk.download('stopwords')

def export_text(doc):
    filepath = str(doc)
    filename = os.path.split(filepath)[1]
    extension = os.path.splitext(filename)[1]

    if extension == ".txt":
        with open(filepath, "r", encoding="utf-8") as f:
            data = f.read()
        return data
    else:
        pass


def get_stopwords():
    all_stopwords = set(nltk.corpus.stopwords.words("english"))
    all_stopwords.add(",")
    all_stopwords.add(".")
    all_stopwords.add("'s")
    all_stopwords.add("us")
    all_stopwords.add("-")
    all_stopwords.add("'ve")
    all_stopwords.add("n't")
    all_stopwords.add("'re")
    all_stopwords.add(";")
    all_stopwords.add("?")
    all_stopwords.add("'ll")
    all_stopwords.add("'")
    all_stopwords.add("''")
    all_stopwords.add("``")
    all_stopwords.add("’")
    all_stopwords.add("'d")
    all_stopwords.add("one")
    all_stopwords.add("'m")
    all_stopwords.add(":")
    all_stopwords.add("!")
    all_stopwords.add("$")
    all_stopwords.add("--")
    all_stopwords.add(r"[0-9]+")

    return all_stopwords


def extract_interesting_words(data, tokenizer):

    words = nltk.word_tokenize(data)
    words_1 = [w.lower() for w in words]

    all_stopwords = get_stopwords()

    filtered_words = [w for w in words_1 if w not in all_stopwords]

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
                # Save word and frequencry
                word_instance = Words(word=w)
                word_instance.document = doc
                word_instance.occurences = freq
                word_instance.save()

                if all_phrases:
                    for sent in all_phrases:
                        # If Word is not embedded in another word in sentence
                        if " "+ w +" " in sent or w +" " in sent or " "+ w in sent:
                            # Save sentence
                            sent_instance = Phrases(phrase=sent)
                            sent_instance.word = word_instance
                            sent_instance.save()

        print("Text analysed.")
    

#if __name__ == '__main__':
#    analyse('6bf5a021-a846-445d-a233-2371d947c8e4')
