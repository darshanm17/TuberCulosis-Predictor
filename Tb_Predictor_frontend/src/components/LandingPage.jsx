// src/LandingPage.jsx
import React, { useState } from "react";
import "./LandingPage.css";
import Home from "./Home";
import About from "./About";
import Predictor from "./Predictor";
import Stats from "./Stats";
import AboutDev from "./AboutDev";
import Contact from "./Contact";

const LandingPage = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  return (
    <div className="landing-page">
      <header className="header">
        <h1>Tuberculosis Predictor</h1>
        <div className="hamburger" onClick={toggleMenu}>
          &#9776;
        </div>
        <nav>
          <ul className={`nav-links ${isMenuOpen ? 'show' : 'collapsed'}`}>
            <li>
              <a href="#home">Home</a>
            </li>
            <li>
              <a href="#about">About</a>
            </li>
            <li>
              <a href="#predict">Predict</a>
            </li>
            <li>
              <a href="#stats">Stats</a>
            </li>
            <li>
              <a href="#symptoms">Symptoms</a>
            </li>
            {/* <li>
              <a href="#about-dev">About Developer</a>
            </li> */}
            <li>
              <a href="#contact">Contact</a>
            </li>
          </ul>
        </nav>
      </header>
      <main>
        <Home />
        <About />
        <Predictor />
        <Stats />
        {/* <AboutDev /> */}
<Contact/>
   
      </main>
      <footer className="footer">
        <p>&copy; 2024 Tuberculosis Predictor. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default LandingPage;
