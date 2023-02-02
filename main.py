from flask import Flask, request, render_template
import numpy as np
import joblib as jb
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Load your trained model
model = jb.load('model.joblib')
le = LabelEncoder()
food = pd.read_csv('food.csv')
le.fit_transform(food['Country'])

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        # Get the input values from the form
        meal_inexpensive = float(request.form["meal_inexpensive"])
        meal_mid_range = float(request.form["meal_mid_range"])
        mc_meal = float(request.form["mc_meal"])
        coke = float(request.form["coke"])
        water_small = float(request.form["water_small"])
        milk = float(request.form["milk"])
        bread = float(request.form["bread"])
        eggs = float(request.form["eggs"])
        cheese = float(request.form["cheese"])
        water_big = float(request.form["water_big"])
        chicken = float(request.form["chicken"])
        apples = float(request.form["apples"])
        oranges = float(request.form["oranges"])
        potato = float(request.form["potato"])
        lettuce = float(request.form["lettuce"])
        cappuccino = float(request.form["cappuccino"])
        rice = float(request.form["rice"])
        tomato = float(request.form["tomato"])
        banana = float(request.form["banana"])
        onion = float(request.form["onion"])
        beef = float(request.form["beef"])

        # Put the inputs into a numpy array
        inputs = np.array([meal_inexpensive, meal_mid_range, mc_meal, coke, water_small, milk, bread, eggs, cheese, water_big, chicken, apples, oranges, potato, lettuce, cappuccino, rice, tomato, banana, onion, beef]).reshape(1, -1)

        # Use the model to make a prediction
        prediction = model.predict(inputs)
        
        # Map the prediction back to a country name (if you have a mapping from label to country name)
        country = le.inverse_transform(prediction)

        return render_template("result.html", prediction=country)

if __name__ == "__main__":
    app.run(debug=True)
