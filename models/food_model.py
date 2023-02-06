import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE,RandomOverSampler
import joblib as jb
import pandas as pd

food = pd.read_csv('categories/food.csv')
food['Take-aways'] = food[["Meal, Inexpensive Restaurant","Meal for 2 People, Mid-range Restaurant, Three-course","McMeal at McDonalds (or Equivalent Combo Meal)"]].mean(axis=1)
food['Drinks'] = food[["Coke/Pepsi (0.33 liter bottle)","Water (0.33 liter bottle) ","Water (1.5 liter bottle)","Cappuccino (regular)"]].mean(axis=1)
food['Dairy and Wheat'] = food[["Milk (regular), (1 liter)","Loaf of Fresh White Bread (500g)","Eggs (regular) (12)","Local Cheese (1kg)"]].mean(axis=1)
food['Fruits and Vegetables'] = food[["Apples (1kg)","Oranges (1kg)","Potato (1kg)","Lettuce (1 head)","Rice (white), (1kg)","Tomato (1kg)","Banana (1kg)","Onion (1kg)"]].mean(axis=1)
food['Meat'] = food[["Chicken Breasts (Boneless, Skinless), (1kg)","Beef Round (1kg) (or Equivalent Back Leg Red Meat)"]].mean(axis=1)
food = food[["Take-aways","Drinks","Dairy and Wheat","Fruits and Vegetables","Meat","Country","Capital"]]
x = food.drop(['Country','Capital'],axis=1)

def categorize_quantiles(df):
    result = pd.DataFrame(index=df.index)
    for col in df.columns:
        quantiles = df[col].quantile([0.25, 0.5, 0.75])
        q1, q2, q3 = quantiles[0.25], quantiles[0.5], quantiles[0.75]
        col_categories = []
        for val in df[col]:
            if val < q1:
                col_categories.append("cheap")
            elif val >= q1 and val < q2:
                col_categories.append("medium")
            elif val >= q2 and val < q3:
                col_categories.append("expensive")
            else:
                col_categories.append("very expensive")
        result[col + '_category'] = col_categories
    return result
f = categorize_quantiles(x)
f_new = pd.concat([f,food[['Country','Capital']]],axis=1)
le2 = LabelEncoder()
# Loop over all the columns in the dataframe
for col in f_new.columns:
    # Check if the column is of type 'object'
    if f_new[col].dtype == 'object':
        # Fit the LabelEncoder on the column
        le2.fit(f_new[col])
        # Transform the column to numerical labels
        f_new[col] = le2.fit_transform(f_new[col])
x_new = f_new.drop(['Country','Capital'],axis=1)
y_new = f_new['Country']

x_train ,x_test,y_train,y_test = train_test_split(x_new,y_new,test_size=0.2,random_state=123)
ros = RandomOverSampler(random_state=123)
x_re, y_re = ros.fit_resample(x_new, y_new)
sm = SMOTE()
x_smo ,y_smo = sm.fit_resample(x_re,y_re)
new_model = RandomForestClassifier(random_state=123,n_estimators=100)
new_model.fit(x_smo,y_smo)
jb.dump(new_model,"models/food.joblib")
print("model saved successfully")
