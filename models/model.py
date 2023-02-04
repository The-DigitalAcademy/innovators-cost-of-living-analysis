from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from imblearn.over_sampling import SMOTE,RandomOverSampler
import joblib as jb
import pandas as pd

food = pd.read_csv('food.csv')

le = LabelEncoder()
food['Country'] = le.fit_transform(food['Country'])
food['Capital'] = le.fit_transform(food['Capital'])

sm = SMOTE(random_state=123)

x = food.drop(['Country','Capital'],axis=1)
y = food['Country']

x_train ,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=123)
ros = RandomOverSampler(random_state=123)
x_resampled, y_resampled = ros.fit_resample(x, y)

x_sm ,y_sm = sm.fit_resample(x_resampled,y_resampled)
model = KNeighborsClassifier(n_neighbors=5)
model.fit(x_sm,y_sm)
jb.dump(model,'model.joblib')
print('model saved successfully saved')