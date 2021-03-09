import string
from flask import Flask, render_template, request

# ----------------------#
# Author: Jorge Nieves
# ----------------------#

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")


@app.route("/similarity", methods=['POST'])
def check_similarity():
    """
    Jaccard Similarity. Utilize sets to find the words that are common in both samples of text (intersection)
    and the ones who are in either one (union).
    """

    # Init stopwords
    stopwords = []
    with open('stopwords.txt', 'r') as file:
        for word in file.read().splitlines():
            stopwords.append(word)

    # Values from POST body
    text_1 = request.form["text_1"]
    text_2 = request.form["text_2"]

    # Remove stopwords
    a_ = ' '.join([ele.lower() for ele in text_1.split() if ele not in stopwords])
    b_ = ' '.join([ele.lower() for ele in text_2.split() if ele not in stopwords])

    # Remove punctuations
    a__ = ''.join([ele for ele in a_ if ele not in string.punctuation])
    b__ = ''.join([ele for ele in b_ if ele not in string.punctuation])

    # Create word set
    a = set(a__.split())
    b = set(b__.split())

    # Compute similarity
    similarity = float(len(a.intersection(b)) / len(a.union(b)))

    print('Similarity Score: {0:.2f} '.format(similarity))

    return '<h1>Similarity Score: {0:.2f}</h1>'.format(similarity)


if __name__ == "__main__":
    app.run(debug=True)
