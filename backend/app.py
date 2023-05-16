from flask import Flask, request, jsonify
import pickle
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'], methods=['GET', 'POST'], allow_headers=['Content-Type'])
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def get_prediction():
    try:
        age = int(request.args.get('age'))
        sex = int(request.args.get('sex'))
        chestPainType = int(request.args.get('chestPainType'))
        restingBloodPressure = int(request.args.get('restingBloodPressure'))
        serumCholesterol = int(request.args.get('serumCholesterol'))
        fastingBloodSugar = int(request.args.get('fastingBloodSugar'))
        restingECG = int(request.args.get('restingECG'))
        maxHeartRate = int(request.args.get('maxHeartRate'))
        exerciseInducedAngina = int(request.args.get('exerciseInducedAngina'))
        stDepression = float(request.args.get('stDepression'))
        slope = int(request.args.get('slope'))
        fluoroscopyVessels = int(request.args.get('fluoroscopyVessels'))
        thalassemia = int(request.args.get('thalassemia'))

        make_prediction = model.predict([[age, sex, chestPainType, restingBloodPressure, serumCholesterol, fastingBloodSugar, restingECG, maxHeartRate, exerciseInducedAngina, stDepression, slope, fluoroscopyVessels, thalassemia]])

        prediction = int(make_prediction[0])

        response = str(prediction)

        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)