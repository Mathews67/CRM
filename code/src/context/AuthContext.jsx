import React, { createContext, useState, useContext, useEffect } from 'react';

// Create the AuthContext
const AuthContext = createContext();

// Create a provider component
export const AuthProvider = ({ children }) => {
  // Initialize authState with null or any default values
  const [authState, setAuthState] = useState({
    token: null, // Store token here, if logged in
    user: null,  // Optionally store user details
  });

  // Function to log in the user and set token and user data
  const loginUser = (token, user) => {
    setAuthState({
      token,
      user,
    });
    localStorage.setItem('authToken', token); // Save token to localStorage
    localStorage.setItem('user', JSON.stringify(user)); // Save user data to localStorage
  };

  // Function to log out the user and clear token and user data
  const logoutUser = () => {
    setAuthState({
      token: null,
      user: null,
    });
    localStorage.removeItem('authToken'); // Remove token from localStorage
    localStorage.removeItem('user'); // Remove user data from localStorage
  };

  // On component mount, check if token exists in localStorage
  useEffect(() => {
    const token = localStorage.getItem('authToken');
    const user = JSON.parse(localStorage.getItem('user'));
    if (token && user) {
      setAuthState({ token, user }); // Set the authState from localStorage if available
    }
  }, []); // This effect runs only once on mount

  return (
    <AuthContext.Provider value={{ authState, loginUser, logoutUser }}>
      {children}
    </AuthContext.Provider>
  );
};

// Custom hook to access the authContext
export const useAuthContext = () => {
  return useContext(AuthContext); // Access the AuthContext using useContext hook
};
