# Text Similarity
This program runs a local web service that takes in two texts and uses a metric to find how similar they are.

### Processing the text
- For both texts, the program removes all
'stopwords' from the text. 'Stopwords' are the most commonly used words in a language. The 'stopword' list used here 
comes from the 'stopwords' used in `nltk.corpus`.

  
- Remove all the punctuation from the text so that it 
can process clean words without punctuation marks.
  

- Utilize the Jaccard Similarity metric to compute the similarity ratio.

### Dependencies
- Must have Python 3.xx installed.
  

- Run `pip install -r requirements.txt` in the console to install required dependencies

### Running the program
- To run this program simple run:
`python3 run_program.py`


- After running this code, open a new browser window and type in:
`http://127.0.0.1:5000/ `


- From this local webpage, enter your two texts and press the `Process` button to compute the similarity ratio.

