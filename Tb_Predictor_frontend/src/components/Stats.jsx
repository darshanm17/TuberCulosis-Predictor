// src/components/Stats.jsx
import React, { useRef, useEffect, useState } from 'react';
import './Stats.css';

export default function Stats() {
  const [isVisible, setIsVisible] = useState(false);
  const [cases, setCases] = useState(1234567); // Example static number
  const [deaths, setDeaths] = useState(123456); // Example static number

  const statsRef = useRef(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsVisible(true);
          observer.unobserve(statsRef.current); // Stop observing after animation
        }
      },
      { threshold: 0.1 }
    );

    if (statsRef.current) {
      observer.observe(statsRef.current);
    }

    return () => {
      if (statsRef.current) {
        observer.unobserve(statsRef.current);
      }
    };
  }, []);

  return (
    <section id="stats" className={`stats ${isVisible ? 'animate' : ''}`} ref={statsRef}>
    <h1>
      Tuberculosis Statistics
    </h1>
      <div className="stat-item">
        <h2 className="stat-number">{cases.toLocaleString()}</h2>
        <p className="stat-label">Cases</p>
      </div>
      <div className="stat-item">
        <h2 className="stat-number">{deaths.toLocaleString()}</h2>
        <p className="stat-label">Deaths</p>
      </div>
    </section>
  );
}
