import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Witness = () => {
  const [witnesses, setWitnesses] = useState([]);
  const [newWitness, setNewWitness] = useState("");

  // Fetch witnesses
  useEffect(() => {
    axios.get('http://localhost:8000/api/witnesses/')
      .then(response => setWitnesses(response.data))
      .catch(error => console.error("Error fetching witnesses:", error));
  }, []);

  // Create new witness
  const handleCreateWitness = () => {
    if (!newWitness.trim()) {
      alert("Witness name cannot be empty");
      return;
    }

    axios.post('http://localhost:8000/api/witnesses/', { name: newWitness })
      .then(response => {
        setWitnesses([...witnesses, response.data]);
        setNewWitness("");
      })
      .catch(error => console.error("Error creating witness:", error));
  };

  // Delete witness
  const handleDeleteWitness = (id) => {
    if (window.confirm("Are you sure you want to delete this witness?")) {
      axios.delete(`http://localhost:8000/api/witnesses/${id}/`)
        .then(() => {
          setWitnesses(witnesses.filter(witness => witness.id !== id));
        })
        .catch(error => console.error("Error deleting witness:", error));
    }
  };

  return (
    <div>
      <h1>Witnesses</h1>
      <input
        type="text"
        value={newWitness}
        onChange={(e) => setNewWitness(e.target.value)}
        placeholder="Enter new witness"
      />
      <button onClick={handleCreateWitness}>Add Witness</button>
      
      <h2>Existing Witnesses</h2>
      <ul>
        {witnesses.length > 0 ? (
          witnesses.map((witness) => (
            <li key={witness.id}>
              {witness.name}
              <button onClick={() => handleDeleteWitness(witness.id)}>Delete</button>
            </li>
          ))
        ) : (
          <li>No witnesses available.</li>
        )}
      </ul>
    </div>
  );
};

export default Witness;
