import pandas as panda
from sklearn.ensemble import RandomForestClassifier

#Importing the dataset
myData = panda.read_csv('heart-disease-data.csv')
#print(myData)

#Checking and managing any missing values
myData.isnull().sum()

#Checking and managing duplicate values
myData = myData.drop_duplicates()

x = myData.drop('target', axis=1)
y = myData['target']

#Training the classifier on the entire dataset
myRF = RandomForestClassifier()
myRF.fit(x,y)

patientData0 = panda.DataFrame ({
    'age': 40,
    'sex': 1,
    'cp': 0,
    'trestbps': 125,
    'chol': 212,
    'fbs': 0,
    'restecg': 1,
    'thalach': 168,
    'exang': 0,
    'oldpeak': 1.0,
    'slope': 2,
    'ca': 2,
    'thal': 3
}, index=[0])

patientData1 = panda.DataFrame ({
    'age': 71,
    'sex': 0,
    'cp': 0,
    'trestbps': 112,
    'chol': 149,
    'fbs': 0,
    'restecg': 1,
    'thalach': 125,
    'exang': 0,
    'oldpeak': 1.6,
    'slope': 1,
    'ca': 0,
    'thal': 2
}, index=[0])

#print(patientData)

#Predict the heart disease risk
rslt = myRF.predict(patientData1)
#print(rslt)

if(rslt == 1):
    print("Heart disease risk detected!")
elif(rslt == 0):
    print("Heart disease risk not detected!")
else:
    print("Something went wrong. Please try again!")