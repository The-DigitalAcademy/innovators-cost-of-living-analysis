import streamlit as st
import joblib as jb
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np


def load_model(model_name):
    return jb.load(f"models/{model_name}.joblib")

model_names = ['food', 'apartment']
feature_lists = {'food': ["Take-aways","Drinks","Dairy and Wheat","Fruits and Vegetables","Meat"], 'apartment': ['Apartment (1 bedroom) in City Centre','Apartment (1 bedroom) Outside of Centre','Apartment (3 bedrooms) in City Centre','Apartment (3 bedrooms) Outside of Centre']}

le = LabelEncoder()
model_name = st.sidebar.selectbox("Select Category:", model_names)
features = feature_lists[model_name]

labels = pd.read_csv('categories/cost-of-living-clean.csv')
labels = labels['Country']

model = load_model(model_name)
le.fit(labels)

category_map = {'cheap': 0, 'medium': 1, 'expensive': 2, 'very expensive': 3}

st.title("Cost of living")

selected_features = []
empty = []

for feature in features:
    category = st.selectbox(f"Categorize {feature}:", list(category_map.keys()))
    selected_features.append((category_map[category]))

with st.form("prediction"):
    submit = st.form_submit_button("Submit")
    if submit:
        predict_proba = model.predict_proba(np.array(selected_features).reshape(1, -1))
        top_10_predictions = np.argsort(predict_proba[0])[-10:][::-1]
        top_10_prediction_labels = le.inverse_transform(top_10_predictions)  


        st.write("Top 10 Predictions:")
        st.write(top_10_prediction_labels)