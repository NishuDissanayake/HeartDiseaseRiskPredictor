import { MDBContainer, MDBRadio } from 'mdb-react-ui-kit';
import './App.css';
import { MDBRow, MDBCol, MDBBtn, MDBInput } from 'mdb-react-ui-kit';

function App() {
  return (
    <div className="App">
      <MDBContainer>
        <MDBRow className="row1">
          <form>
            <MDBRow className='mb-4'>
              <h2 className='head1'>Heart Disease Risk Prediction</h2>
              <MDBCol>
                <MDBInput id='age' label='Age' />
              </MDBCol>
              <MDBCol>
                <select label="sex" className='dpdown'>
                  <option value="">Select your gender</option>
                  <option value="1">Male</option>
                  <option value="0">Female</option>
                </select>
              </MDBCol>
            </MDBRow>

            <MDBRow className='mb-4'>
              <MDBCol>
                <MDBInput id='age' label='Chest Pain Type' />
              </MDBCol>
              <MDBCol>
                <MDBInput id='age' label='Resting Blood Pressure' />
              </MDBCol>
            </MDBRow>

            <MDBRow className='mb-4'>
              <MDBCol>
                <MDBInput id='age' label='Serum Cholesterol (mg/dl)' />
              </MDBCol>
              <MDBCol>
                <MDBInput id='age' label='Fasting Blood Sugar > 120 mg/dl' />
              </MDBCol>
            </MDBRow>

            <MDBRow className='mb-4'>
              <MDBCol>
              <select label="sex" className='dpdown'>
                  <option value="">Resting Electrocardiographic Result</option>
                  <option value="0">0</option>
                  <option value="1">1</option>
                  <option value="2">2</option>
                </select>
              </MDBCol>
              <MDBCol>
                <MDBInput id='age' label='Maximum Heart Rate' />
              </MDBCol>
            </MDBRow>

            <MDBRow className='mb-4'>
              <MDBCol>
                <MDBInput id='age' label='Exercise Induced Angina' />
              </MDBCol>
              <MDBCol>
                <MDBInput id='age' label='ST Depression Induced by Exercise Relative to Rest ' />
              </MDBCol>
            </MDBRow>

            <MDBRow className='mb-4'>
              <MDBCol>
                <MDBInput id='age' label='Slope of the Peak Exercise ST Segment ' />
              </MDBCol>
              <MDBCol>
                <MDBInput id='age' label='Flouroscopy Major Vessels' />
              </MDBCol>
            </MDBRow>

            <MDBRow className='mb-4'>
              <MDBCol>
                <MDBInput id='age' label='Thalassemia' />
              </MDBCol>
            </MDBRow>

            <MDBBtn type='submit' className='mb-4 subBtn' block>
              Predict
            </MDBBtn>

          </form>

          <MDBRow>
            <p className='rsltTxt'>Await Reults...!</p>
          </MDBRow>

        </MDBRow>
      </MDBContainer>
    </div>
  );
}

export default App;
