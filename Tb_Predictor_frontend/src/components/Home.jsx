import React from 'react';
import 'animate.css';
import './Home.css';

export default function Home() {
  return (
    <>
      <section id="home" className="hero animate__animated animate__fadeIn">
        <h2 className="animate__animated animate__fadeInDown">Welcome to the Tuberculosis Predictor</h2>
        <p className="animate__animated animate__fadeInUp">Predict the likelihood of tuberculosis from X-ray images using state-of-the-art machine learning algorithms.</p>
        <a href="#predict" className="cta-button animate__animated animate__pulse animate__infinite">Get Started</a>
        {/* <div class="hover">
        <div class="container">
          <div class="image">
            <img src="https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg" class="img" alt="" />
          </div>
        </div>
      </div> */}
      </section>
    </>
  );
}
