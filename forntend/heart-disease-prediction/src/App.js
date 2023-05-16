import { MDBContainer, MDBRadio } from 'mdb-react-ui-kit';
import './App.css';
import { MDBRow, MDBCol, MDBBtn, MDBInput } from 'mdb-react-ui-kit';
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Swal from 'sweetalert2';


function App() {

  const [prediction, setPrediction] = useState('');
  const [age, setAge] = useState('');
  const [sex, setSex] = useState('');
  const [chestPainType, setCPType] = useState('');
  const [restingBloodPressure, setRestingBP] = useState('');
  const [serumCholesterol, setSerumChol] = useState('');
  const [fastingBloodSugar, setFastingBP] = useState('');
  const [restingECG, setRestingECG] = useState('');
  const [maxHeartRate, setMaxHR] = useState('');
  const [exerciseInducedAngina, setExerciseAngina] = useState('');
  const [stDepression, setSTDep] = useState('');
  const [slope, setSlope] = useState('');
  const [fluoroscopyVessels, setFlouro] = useState('');
  const [thalassemia, setThal] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {

      const params = new URLSearchParams();
      params.append('age', age);
      params.append('sex', sex);
      params.append('chestPainType', chestPainType);
      params.append('restingBloodPressure', restingBloodPressure);
      params.append('serumCholesterol', serumCholesterol);
      params.append('fastingBloodSugar', fastingBloodSugar);
      params.append('restingECG', restingECG);
      params.append('maxHeartRate', maxHeartRate);
      params.append('exerciseInducedAngina', exerciseInducedAngina);
      params.append('stDepression', stDepression);
      params.append('slope', slope);
      params.append('fluoroscopyVessels', fluoroscopyVessels);
      params.append('thalassemia', thalassemia);

      const res = await axios.get("http://localhost:5000/?" + params.toString());
      console.log(res.data);
      setPrediction(res.data);

      setAge("");
      setSex("");
      setCPType("");
      setRestingBP("");
      setSerumChol("");
      setFastingBP("");
      setRestingECG("");
      setMaxHR("");
      setExerciseAngina("");
      setSTDep("");
      setSlope("");
      setFlouro("");
      setThal("");
      Swal.fire({
        title: 'Success!',
        text: 'Predicted successfully!',
        icon: 'success',
        confirmButtonText: 'OK'
      });


    } catch (error) {
      console.log(error);
      Swal.fire({
        title: 'Error!',
        text: 'Prediction failed!',
        icon: 'error',
        confirmButtonText: 'OK'
      });
    }
  };

  return (
    <div className="App">
      <MDBContainer>
        <MDBRow className="row1">
          <form onSubmit={handleSubmit}>
            <MDBRow className='mb-4'>
              <h2 className='head1'>Heart Disease Risk Prediction</h2>
              <MDBCol>
                <MDBInput id='age' name='age' label='Age' value={age} onChange={e => setAge(e.target.value)} required />
              </MDBCol>
              <MDBCol>
                <select id='sex' name='sex' label="sex" className='dpdown' value={sex} onChange={e => setSex(e.target.value)} required>
                  <option value="">Select your gender</option>
                  <option value="1">Male</option>
                  <option value="0">Female</option>
                </select>
              </MDBCol>
            </MDBRow>

            <MDBRow className='mb-4'>
              <MDBCol>
                <MDBInput id='chestPainType' label='Chest Pain Type' value={chestPainType} onChange={e => setCPType(e.target.value)} required />
              </MDBCol>
              <MDBCol>
                <MDBInput id='restingBloodPressure' label='Resting Blood Pressure' value={restingBloodPressure} onChange={e => setRestingBP(e.target.value)} required />
              </MDBCol>
            </MDBRow>

            <MDBRow className='mb-4'>
              <MDBCol>
                <MDBInput id='serumCholesterol' label='Serum Cholesterol (mg/dl)' value={serumCholesterol} onChange={e => setSerumChol(e.target.value)} required />
              </MDBCol>
              <MDBCol>
                <MDBInput id='fastingBloodSugar' label='Fasting Blood Sugar > 120 mg/dl' value={fastingBloodSugar} onChange={e => setFastingBP(e.target.value)} required />
              </MDBCol>
            </MDBRow>

            <MDBRow className='mb-4'>
              <MDBCol>
                <select id="restingECG" label="Restog ECG" className='dpdown' value={restingECG} onChange={e => setRestingECG(e.target.value)} required>
                  <option value="">Resting Electrocardiographic Result</option>
                  <option value="0">0</option>
                  <option value="1">1</option>
                  <option value="2">2</option>
                </select>
              </MDBCol>
              <MDBCol>
                <MDBInput id='maxHeartRate' label='Maximum Heart Rate' value={maxHeartRate} onChange={e => setMaxHR(e.target.value)} required />
              </MDBCol>
            </MDBRow>

            <MDBRow className='mb-4'>
              <MDBCol>
                <MDBInput id='exerciseInducedAngina' label='Exercise Induced Angina' value={exerciseInducedAngina} onChange={e => setExerciseAngina(e.target.value)} required />
              </MDBCol>
              <MDBCol>
                <MDBInput id='stDepression' label='ST Depression Induced by Exercise Relative to Rest ' value={stDepression} onChange={e => setSTDep(e.target.value)} required />
              </MDBCol>
            </MDBRow>

            <MDBRow className='mb-4'>
              <MDBCol>
                <MDBInput id='slope' label='Slope of the Peak Exercise ST Segment ' value={slope} onChange={e => setSlope(e.target.value)} required />
              </MDBCol>
              <MDBCol>
                <MDBInput id='fluoroscopyVessels' label='Flouroscopy Major Vessels' value={fluoroscopyVessels} onChange={e => setFlouro(e.target.value)} required />
              </MDBCol>
            </MDBRow>

            <MDBRow className='mb-4'>
              <MDBCol>
                <MDBInput id='thalassemia' label='Thalassemia' value={thalassemia} onChange={e => setThal(e.target.value)} required />
              </MDBCol>
            </MDBRow>

            <MDBBtn type='submit' className='mb-4 subBtn'>Find Risk Prediction Status
            </MDBBtn>

          </form>

          <MDBRow>
            <p className='rsltTxt'>
              {prediction === 1
                ? 'Heart disease risk detected!'
                : prediction === 0
                  ? 'Heart disease risk not detected!'
                  : 'Awaiting results...'}
            </p>
          </MDBRow>

        </MDBRow>
      </MDBContainer>
    </div>
  );
}

export default App;
