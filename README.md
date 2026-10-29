# Email / SMS Spam Classifier

This is a **portfolio project** to show how I approach a supervised NLP classification problem: cleaning data, exploring it, training models, and wrapping the best one in a small demo UI.

It is **not a production or final deployment**. There is no live email inbox integration, no hosted API, and no security hardening. It is a local demo you can run to try the model.

## What it can do

- Classify a short English message as **Spam** or **Not Spam**
- Walk through the full pipeline in the notebook:
  - Load and clean the SMS Spam Collection dataset (`spam.csv`)
  - Encode labels (`ham` / `spam`)
  - Explore class balance, text length, and word patterns
  - Preprocess text (lowercase, tokenize, drop stopwords/punctuation, stem)
  - Vectorize text with `CountVectorizer`
  - Compare Naive Bayes variants and Extra Trees
- Serve predictions in a simple Streamlit app using the saved Extra Trees model (`model.pkl`) and vectorizer (`vectorizer.pkl`)

On the held-out test set, Extra Trees was the model I saved: about **97.2% accuracy** and **99.2% precision** for the spam class. Those numbers are for this dataset only and should not be treated as production-grade performance.

## How to run the demo

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python -c "import nltk; nltk.download('punkt_tab'); nltk.download('stopwords')"
streamlit run app.py
```

Paste a message, click **Predict**, and the app returns **Spam** or **Not Spam**.

To retrain or inspect the analysis, open `Email_spam_classifier.ipynb`. Jupyter also needs the packages in `requirements.txt`.

## Project files

| File | Role |
| --- | --- |
| `Email_spam_classifier.ipynb` | Data cleaning, EDA, training, evaluation |
| `app.py` | Streamlit demo |
| `requirements.txt` | Python packages for the notebook and app |
| `spam.csv` | Training data |
| `vectorizer.pkl` / `model.pkl` | Saved vectorizer and Extra Trees classifier |

## What this is not

- Not connected to Gmail, Outlook, or any real mailbox
- Not meant to filter real user email at scale
- Not a finished product with tests, monitoring, or a deployed backend

If you are reviewing this as a hiring sample, treat it as evidence of NLP and sklearn workflow, not as a shipping spam filter.
