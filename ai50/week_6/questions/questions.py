'''
AI50 2023
Week 6: parser.py

Complete the implementation of load_files, tokenize, compute_idfs, top_files,
and top_sentences in questions.py.

To Run:
    questions.py corpus
'''

import nltk
import sys
import os
import math
import string
from typing import Dict, List, Set, Tuple


FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    file_contents = {}
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                file_contents[filename] = file.read()

    return file_contents


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.
    Process document by converting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    # Lowercase the text and tokenize it
    words = nltk.tokenize.word_tokenize(document.lower())

    # Get a set of punctuation characters and stopwords
    punctuation = set(string.punctuation)
    stop_words = set(nltk.corpus.stopwords.words("english"))

    # Filter out the punctuation and stopwords
    words = [word for word in words if word not in punctuation and word not in stop_words]

    return words


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    word_counts = {}
    num_documents = len(documents)

    # Count the number of documents that each word appears in
    for document in documents.values():
        seen_words = set()

        for word in document:
            if word not in seen_words:
                seen_words.add(word)
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

    # Calculate IDF for each word
    idfs = {}
    for word, count in word_counts.items():
        idfs[word] = math.log(num_documents / count)

    return idfs


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    file_scores: Dict[str, float] = {}

    for file, words in files.items():
        total_tf_idf = 0
        for word in query:
            if word in idfs:
                total_tf_idf += words.count(word) * idfs[word]
        file_scores[file] = total_tf_idf

    ranked_files = sorted(file_scores.items(), key=lambda x: x[1], reverse=True)
    ranked_files = [x[0] for x in ranked_files]

    return ranked_files[:n]


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to IDF. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    scores = {}
    for sentence, sentwords in sentences.items():
        sentence_score = 0
        for word in query:
            if word in sentwords:
                sentence_score += idfs[word]

        if sentence_score > 0:
            sentence_density = sum(sentwords.count(w) for w in query) / len(sentwords)
            scores[sentence] = (sentence_score, sentence_density)

    sorted_sentences = sorted(scores.items(), key=lambda x: (x[1][0], x[1][1]), reverse=True)
    sorted_sentences = [sentence for sentence, score in sorted_sentences]

    return sorted_sentences[:n]


if __name__ == "__main__":
    main()
