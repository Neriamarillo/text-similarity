import string
from flask import Flask, render_template, request

# ----------------------#
# Author: Jorge Nieves
# ----------------------#

app = Flask(__name__)


def load_stopwords():
    # Init stopwords
    stopwords = []
    with open('stopwords.txt', 'r') as file:
        for word in file.read().splitlines():
            stopwords.append(word)
    return stopwords


def clean_stopwords(text):
    # Remove stopwords
    stopwords = load_stopwords()
    clean_result = ' '.join([ele.lower() for ele in text.split() if ele not in stopwords])
    return clean_result


def remove_punctuations(text):
    # Remove punctuations
    result = ''.join([ele for ele in text if ele not in string.punctuation])
    return result


def compute_similarity(text_1, text_2):
    if not text_1 and not text_2:
        return "Fields were empty. No score to show."
    similarity = float(len(text_1.intersection(text_2)) / len(text_1.union(text_2)))
    return 'Similarity Score: {0:.2f}'.format(similarity)


@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")


@app.route("/similarity", methods=['POST'])
def check_similarity():
    """
    Jaccard Similarity. Utilize sets to find the words that are common in both samples of text (intersection)
    and the ones who are in either one (union).
    """
    # Values from POST body
    text_1 = request.form["text_1"] if request.form["text_1"] else ''
    text_2 = request.form["text_2"] if request.form["text_2"] else ''

    clean_text_1 = set(remove_punctuations(clean_stopwords(text_1)).split())
    clean_text_2 = set(remove_punctuations(clean_stopwords(text_2)).split())

    return '<h1>{}</h1>'.format(compute_similarity(clean_text_1, clean_text_2))


if __name__ == "__main__":
    app.run(debug=True)
