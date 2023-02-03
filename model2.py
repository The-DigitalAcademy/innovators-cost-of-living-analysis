import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from imblearn.over_sampling import SMOTE,RandomOverSampler
import joblib as jb
import pandas as pd

food = pd.read_csv('food.csv')
x = food.drop(['Country','Capital'],axis=1)
def categorize_quantiles(df):
    result = pd.DataFrame(index=df.index)
    for col in df.columns:
        quantiles = df[col].quantile([0.0,0.13,0.25, 0.5,0.38, 0.75,1.0])
        q1, q2, q3,q4,q5,q6,q7 = quantiles[0.0],quantiles[0.13],quantiles[0.25], quantiles[0.5], quantiles[0.38], quantiles[0.75], quantiles[1.00]
        col_categories = []
        for val in df[col]:
            if val < q1:
                col_categories.append("very very cheap")
            elif val >= q1 and val < q2:
                col_categories.append("very cheap")
            elif val >= q3 and val < q4:
                col_categories.append("cheap")
            elif val >= q4 and val < q5:
                col_categories.append("medium")
            elif val >= q5 and val < q6:
                col_categories.append("expensive")
            elif val >= q6 and val < q7:
                col_categories.append("very expensive")
            else:
                col_categories.append("very very expensive")
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
new_model = KNeighborsClassifier(n_neighbors=1)
new_model.fit(x_smo,y_smo)
jb.dump(new_model,"food_model.joblib")
print("model saved successfully")
