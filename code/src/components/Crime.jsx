import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Crime = () => {
  const [crimes, setCrimes] = useState([]);
  const [newCrime, setNewCrime] = useState("");

  // Fetch crimes
  useEffect(() => {
    axios.get('http://localhost:8000/api/crimes/')
      .then(response => setCrimes(response.data))
      .catch(error => console.error("Error fetching crimes:", error));
  }, []);

  // Create new crime
  const handleCreateCrime = () => {
    if (!newCrime.trim()) {
      alert("Crime name cannot be empty");
      return;
    }

    axios.post('http://localhost:8000/api/crimes/', { name: newCrime })
      .then(response => {
        setCrimes([...crimes, response.data]);
        setNewCrime("");
      })
      .catch(error => console.error("Error creating crime:", error));
  };

  // Delete crime
  const handleDeleteCrime = (id) => {
    if (window.confirm("Are you sure you want to delete this crime?")) {
      axios.delete(`http://localhost:8000/api/crimes/${id}/`)
        .then(() => {
          setCrimes(crimes.filter(crime => crime.id !== id));
        })
        .catch(error => console.error("Error deleting crime:", error));
    }
  };

  return (
    <div>
      <h1>Crimes</h1>
      <input
        type="text"
        value={newCrime}
        onChange={(e) => setNewCrime(e.target.value)}
        placeholder="Enter new crime"
      />
      <button onClick={handleCreateCrime}>Add Crime</button>
      
      <h2>Existing Crimes</h2>
      <ul>
        {crimes.length > 0 ? (
          crimes.map((crime) => (
            <li key={crime.id}>
              {crime.name}
              <button onClick={() => handleDeleteCrime(crime.id)}>Delete</button>
            </li>
          ))
        ) : (
          <li>No crimes available.</li>
        )}
      </ul>
    </div>
  );
};

export default Crime;
