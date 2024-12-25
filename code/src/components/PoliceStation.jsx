import React, { useState, useEffect } from 'react';
import axios from 'axios';

const PoliceStation = () => {
  const [policeStations, setPoliceStations] = useState([]);
  const [newStation, setNewStation] = useState("");

  // Fetch police stations
  useEffect(() => {
    axios.get('http://localhost:8000/api/police-stations/')
      .then(response => setPoliceStations(response.data))
      .catch(error => console.error("Error fetching police stations:", error));
  }, []);

  // Create new police station
  const handleCreateStation = () => {
    if (!newStation.trim()) {
      alert("Police station name cannot be empty");
      return;
    }
    axios.post('http://localhost:8000/api/police-stations/', { name: newStation })
      .then(response => {
        setPoliceStations([...policeStations, response.data]);
        setNewStation("");
      })
      .catch(error => console.error("Error creating police station:", error));
  };

  // Delete police station
  const handleDeleteStation = (id) => {
    axios.delete(`http://localhost:8000/api/police-stations/${id}/`)
      .then(() => {
        setPoliceStations(policeStations.filter(station => station.id !== id));
      })
      .catch(error => console.error("Error deleting police station:", error));
  };

  return (
    <div>
      <h1>Police Stations</h1>
      <input
        type="text"
        value={newStation}
        onChange={(e) => setNewStation(e.target.value)}
        placeholder="New Police Station"
      />
      <button onClick={handleCreateStation}>Add Station</button>
      <ul>
        {policeStations.map((station) => (
          <li key={station.id}>
            {station.name} <button onClick={() => handleDeleteStation(station.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PoliceStation;
