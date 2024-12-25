import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Officer = () => {
  const [officers, setOfficers] = useState([]);
  const [newOfficer, setNewOfficer] = useState("");

  // Fetch officers
  useEffect(() => {
    axios.get('http://localhost:8000/api/officers/')
      .then(response => setOfficers(response.data))
      .catch(error => console.error("Error fetching officers:", error));
  }, []);

  // Create new officer
  const handleCreateOfficer = () => {
    if (!newOfficer.trim()) {
      alert("Officer name cannot be empty");
      return;
    }

    axios.post('http://localhost:8000/api/officers/', { name: newOfficer })
      .then(response => {
        setOfficers([...officers, response.data]);
        setNewOfficer("");
      })
      .catch(error => console.error("Error creating officer:", error));
  };

  // Delete officer
  const handleDeleteOfficer = (id) => {
    if (window.confirm("Are you sure you want to delete this officer?")) {
      axios.delete(`http://localhost:8000/api/officers/${id}/`)
        .then(() => {
          setOfficers(officers.filter(officer => officer.id !== id));
        })
        .catch(error => console.error("Error deleting officer:", error));
    }
  };

  return (
    <div>
      <h1>Officers</h1>
      <input
        type="text"
        value={newOfficer}
        onChange={(e) => setNewOfficer(e.target.value)}
        placeholder="Enter new officer"
      />
      <button onClick={handleCreateOfficer}>Add Officer</button>
      
      <h2>Existing Officers</h2>
      <ul>
        {officers.length > 0 ? (
          officers.map((officer) => (
            <li key={officer.id}>
              {officer.name}
              <button onClick={() => handleDeleteOfficer(officer.id)}>Delete</button>
            </li>
          ))
        ) : (
          <li>No officers available.</li>
        )}
      </ul>
    </div>
  );
};

export default Officer;
