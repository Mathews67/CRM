import React, { useState, useEffect } from 'react';
import axios from 'axios';

const CourtCase = () => {
  const [courtCases, setCourtCases] = useState([]);
  const [newCase, setNewCase] = useState("");

  // Fetch court cases
  useEffect(() => {
    axios.get('http://localhost:8000/api/court-cases/')
      .then(response => setCourtCases(response.data))
      .catch(error => console.error("Error fetching court cases:", error));
  }, []);

  // Create new court case
  const handleCreateCase = () => {
    if (!newCase.trim()) {
      alert("Case name cannot be empty");
      return;
    }

    axios.post('http://localhost:8000/api/court-cases/', { name: newCase })
      .then(response => {
        setCourtCases([...courtCases, response.data]);
        setNewCase("");
      })
      .catch(error => console.error("Error creating court case:", error));
  };

  // Delete court case
  const handleDeleteCase = (id) => {
    if (window.confirm("Are you sure you want to delete this case?")) {
      axios.delete(`http://localhost:8000/api/court-cases/${id}/`)
        .then(() => {
          setCourtCases(courtCases.filter(courtCase => courtCase.id !== id));
        })
        .catch(error => console.error("Error deleting court case:", error));
    }
  };

  return (
    <div>
      <h1>Court Cases</h1>
      <input
        type="text"
        value={newCase}
        onChange={(e) => setNewCase(e.target.value)}
        placeholder="Enter new court case"
      />
      <button onClick={handleCreateCase}>Add Case</button>
      
      <h2>Existing Court Cases</h2>
      <ul>
        {courtCases.length > 0 ? (
          courtCases.map((courtCase) => (
            <li key={courtCase.id}>
              {courtCase.name}
              <button onClick={() => handleDeleteCase(courtCase.id)}>Delete</button>
            </li>
          ))
        ) : (
          <li>No court cases available.</li>
        )}
      </ul>
    </div>
  );
};

export default CourtCase;
