import streamlit as st
import joblib as jb
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np

model = jb.load("food_model.joblib")
le = LabelEncoder()
food = pd.read_csv('food.csv')
le.fit(food['Country'])

features = ["Take-aways","Drinks","Dairy and Wheat","Fruits and Vegetables","Meat"]

category_map = {'inexpensive': 0,'very cheap': 1,'cheap': 2, 'medium': 3, 'expensive': 4, 'very expensive': 5,'luxury': 6}
features_map = {"Take-aways" : 3 , "Drinks" : 4 , "Dairy and Wheat" : 4, "Fruits and Vegetables" : 8 ,"Meat" : 2}

selected_features = []

st.title("Categorize Features")

reference_list = ["meal_inexpensive", "meal_mid_range", "mc_meal", "coke", "water_small", "milk", "bread", "eggs", "cheese", "water_big", "chicken", "apples", "oranges", "potato", "lettuce", "cappuccino", "rice", "tomato", "banana", "onion", "beef"]

for feature in features:
    category = st.selectbox(f"Categorize {feature}:", list(category_map.keys()))
    for i in range(features_map[feature]):
        reference_item = reference_list[i]
        selected_features.append((reference_item, category_map[category]))

selected_features_sorted = sorted(selected_features, key=lambda x: reference_list.index(x[0]))
selected_features_sorted = [f[1] for f in selected_features_sorted]
predict = model.predict(np.array(selected_features_sorted).reshape(1, -1))
prediction = le.inverse_transform(predict)

st.write("Selected Features:")
st.write(prediction)
