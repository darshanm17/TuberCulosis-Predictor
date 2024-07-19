// src/Predictor.jsx
import React, { useState } from 'react';
import axios from 'axios';
import './Predictor.css';

export default function Predictor() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [previewImage, setPreviewImage] = useState(null);
  const [prediction, setPrediction] = useState('');

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
    setPreviewImage(URL.createObjectURL(event.target.files[0]));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!selectedFile) {
      alert('Please upload an X-ray image first!');
      return;
    }

    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      const response = await axios.post('http://localhost:5000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      const result = response.data.prediction;
      setPrediction(result);

      // Play the appropriate sound based on the prediction
      playSound(result);
    } catch (error) {
      console.error('There was an error uploading the file!', error);
    }
  };

  const playSound = (result) => {
    const audio = new Audio(
      result.toLowerCase() === 'tuberculosis' 
        ? '/sounds/alarm.mp3' 
        : '/sounds/congrats.mp3'
    );
    audio.play();
  };

  return (
    <>
      <section id="predict" className="predict">
        <div className="App">
          <h1>Tuberculosis Predictor</h1>
          <form onSubmit={handleSubmit}>
            <input type="file" onChange={handleFileChange} />
            {previewImage && <img src={previewImage} alt="Preview" style={{ maxWidth: '100%', marginTop: '10px' }} />}
            <button type="submit">Upload and Predict</button>
          </form>
          {prediction && <h2>Prediction: {prediction}</h2>}
        </div>
      </section>
    </>
  );
}
