import React, { useState, useEffect } from 'react';
import axios from 'axios';

const CrimeCategory = () => {
  const [crimeCategories, setCrimeCategories] = useState([]);
  const [newCategory, setNewCategory] = useState("");
  
  // Fetch crime categories
  useEffect(() => {
    axios.get('http://localhost:8000/api/crime-categories/')
      .then(response => setCrimeCategories(response.data))
      .catch(error => console.error("Error fetching crime categories:", error));
  }, []);
  
  // Create new crime category
  const handleCreateCategory = () => {
    if (!newCategory.trim()) {
      alert("Category name cannot be empty");
      return;
    }
    
    axios.post('http://localhost:8000/api/crime-categories/', { name: newCategory })
      .then(response => {
        setCrimeCategories([...crimeCategories, response.data]);
        setNewCategory("");
      })
      .catch(error => console.error("Error creating category:", error));
  };
  
  // Delete category
  const handleDeleteCategory = (id) => {
    if (window.confirm("Are you sure you want to delete this category?")) {
      axios.delete(`http://localhost:8000/api/crime-categories/${id}/`)
        .then(() => {
          setCrimeCategories(crimeCategories.filter(category => category.id !== id));
        })
        .catch(error => console.error("Error deleting category:", error));
    }
  };

  return (
    <div>
      <h1>Crime Categories</h1>
      <input
        type="text"
        value={newCategory}
        onChange={(e) => setNewCategory(e.target.value)}
        placeholder="Enter new category"
      />
      <button onClick={handleCreateCategory}>Add Category</button>
      
      <h2>Existing Categories</h2>
      <ul>
        {crimeCategories.length > 0 ? (
          crimeCategories.map((category) => (
            <li key={category.id}>
              {category.name}
              <button onClick={() => handleDeleteCategory(category.id)}>Delete</button>
            </li>
          ))
        ) : (
          <li>No crime categories available.</li>
        )}
      </ul>
    </div>
  );
};

export default CrimeCategory;
