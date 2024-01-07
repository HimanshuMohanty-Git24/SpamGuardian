# Import necessary libraries
import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

# Load NLTK data
nltk.download('stopwords')
nltk.download('punkt')

# Load stopwords and create PorterStemmer instance
stop_words = set(stopwords.words('english'))
ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

try:
    tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
    model = pickle.load(open('model.pkl', 'rb'))
except Exception as e:
    st.error(f"Error loading model or vectorizer: {str(e)}")


st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):
    if not input_sms:
        st.warning("Please enter a message before predicting.")
    else:
        # Preprocess text
        transformed_sms = transform_text(input_sms)

        # Vectorize text
        vector_input = tfidf.transform([transformed_sms])

        # Predict
        result = model.predict(vector_input)[0]

        # Display result
        if result == 1:
            st.header("Spam")
        else:
            st.header("Not Spam")