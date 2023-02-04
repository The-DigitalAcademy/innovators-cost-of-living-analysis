import streamlit as st
import joblib as jb
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np

model = jb.load("food_model2.joblib")
le = LabelEncoder()
food = pd.read_csv('categories/food.csv')
le.fit(food['Country'])

features = ["Take-aways","Drinks","Dairy and Wheat","Fruits and Vegetables","Meat"]

category_map = {'cheap': 0, 'medium': 1, 'expensive': 2, 'very expensive': 3}


selected_features = []

for feature in features:
    category = st.selectbox(f"Categorize {feature}:", list(category_map.keys()))
    
    selected_features.append((category_map[category]))

predict_proba = model.predict_proba(np.array(selected_features).reshape(1, -1))
top_10_predictions = np.argsort(predict_proba[0])[-10:][::-1]
top_10_prediction_labels = le.inverse_transform(top_10_predictions)

st.write("Top 10 Predictions:")
st.write(top_10_prediction_labels)
