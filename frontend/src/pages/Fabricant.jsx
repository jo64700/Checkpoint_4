import React from 'react'
import NavBar from '../components/navBar/NavBar'
import { useEffect, useState } from 'react';

const Fabricant = () => {
  const [voitures, setVoitures] = useState([]);

  useEffect(() => {
    // Fonction pour récupérer les données des voitures depuis l'API
    const fetchVoitures = async () => {
      try {
        const response = await fetch('/api/voitures/');
        const data = await response.json();
        setVoitures(data);
      } catch (error) {
        console.error('Erreur lors de la récupération des données des voitures :', error);
      }
    };

    // Appel de la fonction pour récupérer les données des voitures lors du chargement du composant
    fetchVoitures();
  }, []);

  return (
    <div className='navbar-container'>
      {/* Affichage des données des voitures */}
      <ul>
        {voitures.map((voiture) => (
          <li key={voiture.id}>
            {voiture.modele} - {voiture.prix_depart}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Fabricant