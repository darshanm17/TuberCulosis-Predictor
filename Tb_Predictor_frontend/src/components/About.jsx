import React from 'react';
import './About.css';

export default function About() {
  return (
    <section id="about" className="about">
      <div className="scrolling-background"></div>
      <div className="content">
        <h2>About Us</h2>
        <p>Our tool leverages advanced algorithms to provide accurate predictions for tuberculosis based on X-ray images. Our goal is to assist healthcare professionals in early detection and treatment of tuberculosis.</p>
      </div>
    </section>
  );
}
