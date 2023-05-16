#Importing necessary libraries
import pandas as panda
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import matplotlib.pyplot as plt

#Importing the dataset
myData = panda.read_csv('heart-disease-data.csv')
#print(myData)


#Checking and managing any missing values
myData.isnull().sum()


#Checking and managing duplicate values
#duplicate_data = myData.duplicated().any()
#print(duplicate_data)

myData = myData.drop_duplicates()
#duplicate_data = myData.duplicated().any()
#print(duplicate_data)


#Preprocessing the data
categorical_col_list = []
numerical_col_list = []

for column in myData.columns:
    if myData[column].nunique() <= 10:
        categorical_col_list.append(column)
    else:
        numerical_col_list.append(column)

#print(categorical_col_list)
#print(numerical_col_list)


#Encloding the categorical data
#print(myData['cp'].unique())

#removing already binary columns
categorical_col_list.remove('sex')
categorical_col_list.remove('target')

myData = panda.get_dummies(myData, columns=categorical_col_list, drop_first=True)
#print(myData.head())

# Convert True/False values to 1/0
myData = myData.astype(int)
#print(myData.head())

#Feature scaling
sScaler = StandardScaler()
myData[numerical_col_list] = sScaler.fit_transform(myData[numerical_col_list])
#print(myData.head())


#Splitting the data for training and testing
x = myData.drop('target', axis=1)
#print(x)
y = myData['target']
#print(y)


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
"""
print(x_train)
print(x_test)
print(y_train)
print(y_test)
"""


#Logistic Regression

lr = LogisticRegression()

#Training data
lr.fit(x_train, y_train)

y_prediction1 = lr.predict(x_test)
#print(y_prediction1)

#Checking accuracy

lrAccuracy = accuracy_score(y_test, y_prediction1)
#print("Logistic Regression prediction accuracy: " + str(lrAccuracy) + ".")


#Support Vector Classifier
svm = svm.SVC()

#Training data
svm.fit(x_train, y_train)

y_prediction2 = svm.predict(x_test)

#Checking accuracy
svmAccuracy = accuracy_score(y_test, y_prediction2)
#print("Support Vector Classifier prediction accuracy: " + str(svmAccuracy) + ".")



"""
knc2score = []

for k in range(1, 40):
    knc2 = KNeighborsClassifier(n_neighbors=k)
    knc2.fit(x_train, y_train)
    y_pred_knc2 = knc2.predict(x_test)
    knc2score.append(accuracy_score(y_test, y_pred_knc2))

print(knc2score)
print(knc2score[15])
"""


#KNeighbors Classifier
knc = KNeighborsClassifier(n_neighbors=16)

#Training data
knc.fit(x_train, y_train)

y_prediction3 = knc.predict(x_test)

#Checking accuracy
kncAccuracy = accuracy_score(y_test, y_prediction3)
#print("KNeighbors Classifier prediction accuracy: " + str(kncAccuracy) + ".")


#Decision Tree
dt = DecisionTreeClassifier()

#Training data
dt.fit(x_train, y_train)

y_prediction4 = dt.predict(x_test)

#Checking accuracy
dtAccuracy = accuracy_score(y_test, y_prediction4)
#print("Desicion Tree prediction accuracy: " + str(dtAccuracy) + ".")


#Random Forest
rf = RandomForestClassifier()

#Training data
rf.fit(x_train, y_train)

y_prediction5 = rf.predict(x_test)

#Checking accuracy
rfAccuracy = accuracy_score(y_test, y_prediction5)
#print("Random Forest prediction accuracy: " + str(rfAccuracy) + ".")


#Non-Linear Machine Learning Algorithms without preprocessing
MyDataWP = panda.read_csv('heart-disease-data.csv')
#print(MyDataWP)

MyDataWP = MyDataWP.drop_duplicates()
#print(MyDataWP.shape)

xWP = MyDataWP.drop('target', axis=1)
yWP = MyDataWP['target']
#print(xWP)
#print(yWP)

xWP_train, xWP_test, yWP_train, yWP_test = train_test_split(xWP, yWP, test_size=0.2, random_state=42)

#Decision Tree without preprocessing data
dtWP = DecisionTreeClassifier()

#Training data
dtWP.fit(xWP_train, yWP_train)

y_prediction4WP = dtWP.predict(xWP_test)

#Checking accuracy
dtAccuracyWP = accuracy_score(yWP_test, y_prediction4WP)
#print("Desicion Tree prediction accuracy without preprocessing data: " + str(dtAccuracyWP) + ".")

#Random Forest without preprocessing data
rfWP = RandomForestClassifier()

#Training data
rfWP.fit(xWP_train, yWP_train)

y_prediction5WP = rfWP.predict(xWP_test)

#Checking accuracy
rfAccuracyWP = accuracy_score(yWP_test, y_prediction5WP)
#print("Random Forest prediction accuracy without preprocessing data: " + str(rfAccuracyWP) + ".")

#Presenting the findings
finalized_data = panda.DataFrame({'Model': ['LR', 'SVM', 'KNN', 'DT1', 'RF1', 'DT2', 'RF2'], 'Accuracy': [accuracy_score(yWP_test, y_prediction1), accuracy_score(yWP_test, y_prediction2), accuracy_score(yWP_test, y_prediction3), accuracy_score(yWP_test, y_prediction4), accuracy_score(yWP_test, y_prediction5), accuracy_score(yWP_test, y_prediction4WP), accuracy_score(yWP_test, y_prediction5WP)]})
print(finalized_data)

#Plotting to find the best algorithm for the dataset
sns.barplot(x=finalized_data['Model'], y=finalized_data['Accuracy'])
plt.show()

#Since the highest accuracy is from random forest without using preprocssing, it is selected for produciton
