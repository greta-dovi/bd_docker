import pandas as pd
import spacy
import re
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay, confusion_matrix
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pathlib

results_dir = pathlib.Path("results")
results_dir.mkdir(exist_ok=True)

nlp = spacy.load("en_core_web_md")

raw_data = pd.read_csv("all_kindle_review.csv")

df = raw_data.iloc[:, 4:6]

df.loc[df["rating"] <= 3, "rating"] = 0
df.loc[df["rating"] > 3, "rating"] = 1

df["reviewText"] = df["reviewText"].str.lower()

df["reviewText"] = df["reviewText"].apply(lambda x: re.sub(r"(?:(?!\b['‘’]\b)[\W_])+", ' ', x).strip())
df["reviewText"] = df["reviewText"].apply(lambda x: re.sub(r'[\s+]', ' ', x).strip())


def remove_stop_words(sentence):
    doc = nlp(sentence)
    filtered_tokens = [token for token in doc if not token.is_stop]
    return " ".join([token.text for token in filtered_tokens])


df["filtered"] = df["reviewText"].apply(remove_stop_words)


def lemmatize(sentence):
    doc = nlp(sentence)
    return " ".join([token.lemma_ for token in doc])

df["lemmas"] = df["filtered"].apply(lemmatize)

# BOW on lemmatized
y = df["rating"]

bow_vec = CountVectorizer(max_df=0.9, min_df=2, max_features=1000) # does the vectorization
bow = bow_vec.fit_transform(df["lemmas"]) # does the vectorization

xtrain_bow, xval_bow, ytrain, yval = train_test_split(bow, y, random_state=123, test_size=0.2)

model = LogisticRegression(max_iter=1000)
model.fit(xtrain_bow, ytrain)

# Evaluate the model
y_pred = model.predict(xval_bow)
accuracy_bow = accuracy_score(yval, y_pred)
report_bow = classification_report(yval, y_pred)
conf_mat = confusion_matrix(yval, y_pred)
cm_display = ConfusionMatrixDisplay(conf_mat, display_labels=[0, 1])
plot = cm_display.plot(cmap="Blues")
plot.figure_.savefig('results/bow_confusion.jpg')


# TFIDF
tfidf_vec = TfidfVectorizer(max_df=0.9, min_df=2, max_features=1000)
tfidf = tfidf_vec.fit_transform(df["lemmas"])

tfidf_dense = tfidf.toarray()

xtrain_tfidf, xval_tfidf, ytrain, yval = train_test_split(tfidf_dense, y, random_state=123, test_size=0.2)

model = LogisticRegression(max_iter=1000)
model.fit(xtrain_tfidf, ytrain)

# Evaluate the model
y_pred = model.predict(xval_tfidf)
accuracy_tfidf = accuracy_score(yval, y_pred)
report_tfidf = classification_report(yval, y_pred)
conf_mat = confusion_matrix(yval, y_pred)
cm_display = ConfusionMatrixDisplay(conf_mat, display_labels=[0, 1])
plot = cm_display.plot(cmap="Blues")
plot.figure_.savefig('results/tfidf_confusion.jpg')


# output

with open(results_dir / "results.txt", 'w') as f:
    f.writelines(["Bag-of-words results:\n", f"Metrics\n: {report_bow}",
                  "\nTF-IDF results:\n", f"Metrics\n: {report_tfidf}"])