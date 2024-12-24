import React, { createContext, useState, useContext, useEffect } from 'react';

// Create the AuthContext
const AuthContext = createContext();

// Create a provider component
export const AuthProvider = ({ children }) => {
  const [authState, setAuthState] = useState({
    token: null,
    user: null,
  });

  // Function to log in the user
  const loginUser = (token, user) => {
    try {
      setAuthState({ token, user });
      console.log('Setting authState:', { token, user }); // Log the state being set

      localStorage.setItem('authToken', token);
      localStorage.setItem('user', JSON.stringify(user));
    } catch (error) {
      console.error('Error saving user data to localStorage:', error);
    }
  };

  // Function to log out the user
  const logoutUser = () => {
    try {
      setAuthState({ token: null, user: null });

      localStorage.removeItem('authToken');
      localStorage.removeItem('user');
    } catch (error) {
      console.error('Error removing user data from localStorage:', error);
    }
  };

  // Check localStorage for existing token and user data
  useEffect(() => {
    try {
      const token = localStorage.getItem('authToken');
      const user = JSON.parse(localStorage.getItem('user'));
      if (token && user) {
        setAuthState({ token, user });
        console.log('Retrieved authState from localStorage:', { token, user }); // Log retrieved state
      }
    } catch (error) {
      console.error('Error retrieving user data from localStorage:', error);
    }
  }, []);

  return (
    <AuthContext.Provider value={{ authState, loginUser, logoutUser }}>
      {children}
    </AuthContext.Provider>
  );
};

// Custom hook to use the AuthContext
export const useAuthContext = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuthContext must be used within an AuthProvider');
  }
  return context;
};
