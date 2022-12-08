import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

leaf_dataset = pd.read_csv('C:/Users/skrbm/Downloads/leaf_dataset.csv')

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

#Pre-PCA Accuracy list
preAccuracyList = []

#Pre-PCA
svc = SVC(kernel="linear")
svc.fit(x_train_scaled, y_train)
preAccuracyList.append(svc.score(x_test_scaled, y_test)*100)

#Multilayer Perceptron Classifier
nnc=MLPClassifier(hidden_layer_sizes=(7), activation="relu", max_iter=10000)
nnc.fit(x_train_scaled, y_train)
preAccuracyList.append(nnc.score(x_test_scaled, y_test)*100)

#Random Forest
rfc = RandomForestClassifier(n_estimators=70)
rfc.fit(x_train_scaled, y_train)
preAccuracyList.append(rfc.score(x_test_scaled, y_test)*100)


#PCA
pca = PCA(n_components=8) #16 columns present
pca.fit(x_train_scaled)
x_train_scaled_pca = pca.transform(x_train_scaled)
pca.fit(x_test_scaled)
x_test_scaled_pca = pca.transform(x_test_scaled)

#Post-Pca Accuracy List
postAccuracyList = []

#SVM
svc = SVC(kernel="linear")
svc.fit(x_train_scaled_pca, y_train)
postAccuracyList.append(svc.score(x_test_scaled_pca, y_test)*100)

#MPLC
nnc=MLPClassifier(hidden_layer_sizes=(7), activation="relu", max_iter=10000)
nnc.fit(x_train_scaled_pca, y_train)
postAccuracyList.append(nnc.score(x_test_scaled_pca, y_test)*100)

#Random Forest
rfc = RandomForestClassifier(n_estimators=70)
rfc.fit(x_train_scaled_pca, y_train)
postAccuracyList.append(rfc.score(x_test_scaled_pca, y_test)*100)


#Accuracy Barchart

classifiers = ["SVM", "Neural Network", "Random Forest"]
x = np.arange(len(classifiers))
width = 0.1

fig, ax = plt.subplots()
rect1 = ax.bar(x - width/2, preAccuracyList, width, label='Pre-PPC')
rect2 = ax.bar(x + width/2, postAccuracyList, width, label='Post-PPC')

ax.set_ylabel('Accuracy(%)')
ax.set_title('Accuracy by classifiers and pre/post PPC reduction')
ax.set_xticks(x)
ax.set_xticklabels(classifiers)
ax.legend()


fig.tight_layout()

plt.show()
