import json

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.calibration import CalibratedClassifierCV

from joblib import load


def get_prediction_from_text(text: str, model: CalibratedClassifierCV, tfidf: TfidfVectorizer, categories: dict):
    """
    The text will be a string but for the model I will make it a list with one value
    :param text:
    :param model:
    :param tfidf:
    :param categories:
    :return:
    """
    if isinstance(text, str):
        text = [text]
    feature = tfidf.transform(text).toarray()
    prediction = model.predict(feature)
    probabilities = model.predict_proba(feature)
    for idx, prediction in enumerate(prediction):
        cat_proba = round(probabilities[idx].max(), 2)
        if cat_proba < 0.06:
            cat_prediction = 'None'
        else:
            cat_prediction = categories[str(prediction)]
    return (cat_prediction, cat_proba)


def main():
    model = load('models/svcmodel.joblib')
    tfidf = load('models/tfidfmodel.joblib')
    with open('categories.json', 'r') as f:
        categories = json.load(f)
    text = 'Tienda De Ropa en Barcelona'
    print(get_prediction_from_text(text, model, tfidf, categories))
    pass


if __name__ == '__main__':
    main()
