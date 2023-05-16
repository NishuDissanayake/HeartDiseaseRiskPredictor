import pandas as panda
from sklearn.ensemble import RandomForestClassifier
import pickle

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

patientData = panda.DataFrame ({
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

#print(patientData)

#Predict the heart disease risk
rslt = myRF.predict(patientData)
#print(rslt)

if(rslt == 1):
    print("Heart disease risk detected!")
elif(rslt == 0):
    print("Heart disease risk not detected!")
else:
    print("Something went wrong. Please try again!")

#Save the file
filename = "model.pkl"
pickle.dump(myRF, open(filename, 'wb'))

#Load the saved model
loading_model = pickle.load(open("model.pkl", 'rb'))

patientData = panda.DataFrame ({
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

#print(patientData)

#Predict the heart disease risk
rslt = loading_model.predict(patientData)
#print(rslt)

if(rslt == 1):
    print("Heart disease risk detected!")
elif(rslt == 0):
    print("Heart disease risk not detected!")
else:
    print("Something went wrong. Please try again!")