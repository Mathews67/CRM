import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  // State for storing users and crime categories
  const [users, setUsers] = useState([]);
  const [categories, setCategories] = useState([]);

  // Fetch users and crime categories when the component mounts
  useEffect(() => {
    // Fetch users from the API
    axios.get('http://localhost:8000/api/users/')
      .then((response) => {
        setUsers(response.data);
      })
      .catch((error) => {
        console.error('There was an error fetching the users!', error);
      });

    // Fetch crime categories from the API
    axios.get('http://localhost:8000/api/crime-categories/')
      .then((response) => {
        setCategories(response.data);
      })
      .catch((error) => {
        console.error('There was an error fetching the crime categories!', error);
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Crime Reporting System</h1>
      </header>

      {/* User List */}
      <section className="user-list">
        <h2>User List</h2>
        <ul>
          {users.length > 0 ? (
            users.map((user) => (
              <li key={user.id}>
                {user.username} - {user.role}
              </li>
            ))
          ) : (
            <li>Loading users...</li>
          )}
        </ul>
      </section>

      {/* Crime Category List */}
      <section className="crime-category-list">
        <h2>Crime Categories</h2>
        <ul>
          {categories.length > 0 ? (
            categories.map((category) => (
              <li key={category.id}>
                <strong>{category.category_name}</strong>: {category.description}
              </li>
            ))
          ) : (
            <li>Loading crime categories...</li>
          )}
        </ul>
      </section>
    </div>
  );
}

export default App;
