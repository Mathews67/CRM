import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Complaints = () => {
  const [complaints, setComplaints] = useState([]);
  const [newComplaint, setNewComplaint] = useState("");

  // Fetch complaints
  useEffect(() => {
    axios.get('http://localhost:8000/api/complaints/')
      .then(response => setComplaints(response.data))
      .catch(error => console.error("Error fetching complaints:", error));
  }, []);

  // Create new complaint
  const handleCreateComplaint = () => {
    if (!newComplaint.trim()) {
      alert("Complaint description cannot be empty");
      return;
    }
    axios.post('http://localhost:8000/api/complaints/', { description: newComplaint })
      .then(response => {
        setComplaints([...complaints, response.data]);
        setNewComplaint("");
      })
      .catch(error => console.error("Error creating complaint:", error));
  };

  // Delete complaint
  const handleDeleteComplaint = (id) => {
    axios.delete(`http://localhost:8000/api/complaints/${id}/`)
      .then(() => {
        setComplaints(complaints.filter(complaint => complaint.id !== id));
      })
      .catch(error => console.error("Error deleting complaint:", error));
  };

  return (
    <div>
      <h1>Complaints</h1>
      <input
        type="text"
        value={newComplaint}
        onChange={(e) => setNewComplaint(e.target.value)}
        placeholder="New Complaint"
      />
      <button onClick={handleCreateComplaint}>Add Complaint</button>
      <ul>
        {complaints.map((complaint) => (
          <li key={complaint.id}>
            {complaint.description} <button onClick={() => handleDeleteComplaint(complaint.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Complaints;
