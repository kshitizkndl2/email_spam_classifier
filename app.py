import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk

ps = PorterStemmer()
cv = pickle.load(open('vectorizer.pkl','rb'))
etc = pickle.load(open('model.pkl','rb'))


sms = st.text_input("Enter the message")
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
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
    return y
st.title("Email Spam Classifier")
if st.button("Predict"):
    transformed_sms = transform_text(sms)
    transformed_sms = " ".join(transformed_sms)
    vector_input = cv.transform([transformed_sms]).toarray()
    model_predict = etc.predict(vector_input)[0]
    if model_predict == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")



