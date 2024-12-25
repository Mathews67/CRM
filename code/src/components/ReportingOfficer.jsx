import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ReportingOfficer = () => {
  const [reportingOfficers, setReportingOfficers] = useState([]);
  const [newOfficer, setNewOfficer] = useState("");

  // Fetch reporting officers
  useEffect(() => {
    axios.get('http://localhost:8000/api/reporting-officers/')
      .then(response => setReportingOfficers(response.data))
      .catch(error => console.error("Error fetching reporting officers:", error));
  }, []);

  // Create new reporting officer
  const handleCreateOfficer = () => {
    if (!newOfficer.trim()) {
      alert("Officer name cannot be empty");
      return;
    }

    axios.post('http://localhost:8000/api/reporting-officers/', { name: newOfficer })
      .then(response => {
        setReportingOfficers([...reportingOfficers, response.data]);
        setNewOfficer("");
      })
      .catch(error => console.error("Error creating reporting officer:", error));
  };

  // Delete reporting officer
  const handleDeleteOfficer = (id) => {
    if (window.confirm("Are you sure you want to delete this officer?")) {
      axios.delete(`http://localhost:8000/api/reporting-officers/${id}/`)
        .then(() => {
          setReportingOfficers(reportingOfficers.filter(officer => officer.id !== id));
        })
        .catch(error => console.error("Error deleting reporting officer:", error));
    }
  };

  return (
    <div>
      <h1>Reporting Officers</h1>
      <input
        type="text"
        value={newOfficer}
        onChange={(e) => setNewOfficer(e.target.value)}
        placeholder="Enter new reporting officer"
      />
      <button onClick={handleCreateOfficer}>Add Officer</button>
      
      <h2>Existing Reporting Officers</h2>
      <ul>
        {reportingOfficers.length > 0 ? (
          reportingOfficers.map((officer) => (
            <li key={officer.id}>
              {officer.name}
              <button onClick={() => handleDeleteOfficer(officer.id)}>Delete</button>
            </li>
          ))
        ) : (
          <li>No reporting officers available.</li>
        )}
      </ul>
    </div>
  );
};

export default ReportingOfficer;
