import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

leaf_dataset = pd.read_csv('C:/Users/skrbm/Downloads/leaf_dataset.csv')
leaf_dataset.head(3)

leaf_dataset.isnull().sum()
leaf_dataset.shape
leaf_dataset.isnull().sum()


impute = SimpleImputer(missing_values=np.nan, strategy='mean')
impute.fit(leaf_dataset[['Elongation']])
leaf_dataset['Elongation'] = impute.transform(leaf_dataset[['Elongation']])
impute.fit(leaf_dataset[['Average Contrast']])
leaf_dataset['Average Contrast'] = impute.transform(leaf_dataset[['Average Contrast']])
impute.fit(leaf_dataset[['Maximal Indentation Depth']])
leaf_dataset['Maximal Indentation Depth'] = impute.transform(leaf_dataset[['Maximal Indentation Depth']])
impute.fit(leaf_dataset[['Lobedness']])
leaf_dataset['Lobedness'] = impute.transform(leaf_dataset[['Lobedness']])

#No categorical features present

#This is labels
y=leaf_dataset.iloc[:,0]
y

#This is features
x=leaf_dataset.loc[:,leaf_dataset.columns != 'Class(species)']
x

x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.25,random_state=42)

scaler = MinMaxScaler()
scaler.fit(x_train)

x_train_scaled=scaler.transform(x_train)


x_test_scaled=scaler.transform(x_test)

# Lab 5

# Classification using logistic regression

logRegress=LogisticRegression(max_iter=1000)
logRegress.fit(x_train,y_train)
y_predict_lg=logRegress.predict(x_test)

print(y_predict_lg)
lg_accuracy_percent = accuracy_score(y_test, y_predict_lg)*10
print("\nAccuracy Percent:", lg_accuracy_percent)

# Classification using Decision Tree

dtc = DecisionTreeClassifier(criterion='entropy',random_state=1)
dtc.fit(x_train,y_train)
y_predict_dtc = dtc.predict(x_test)
print("\n",y_predict_dtc)
dtc_accuracy_percent = accuracy_score(y_predict_dtc,y_test)*100
print("\nAccuracy Percent:", dtc_accuracy_percent)

# Bar Chart

sns.set_theme(style="whitegrid")
barplotData = pd.DataFrame.from_dict({'cols': ['Logistic Regression', 'Decision Tree'], 'values': [lg_accuracy_percent, dtc_accuracy_percent]})
barChart = sns.barplot(x = 'cols', y = 'values', data = barplotData)
plt.xlabel("Models")
plt.ylabel("Accuracy(%)")
plt.title("Models Accuracy Graph")
plt.show()