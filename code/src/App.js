import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuthContext } from './context/AuthContext';
import Login from './components/Login';
import AdminDashboard from './components/AdminDashboard';
import './App.css';

function App() {
  return (
    <AuthProvider>
      <Router>
        <div className="App">
          <header className="bg-gray-800 text-white py-4">
            <h1 className="text-2xl font-bold text-center">
              Criminal Investigation System
            </h1>
          </header>

          <main className="container mx-auto px-4">
            <Routes>
              <Route
                path="/login"
                element={
                  <Login 
                    onLoginSuccess={({ token, user, isAdmin }) => {
                      if (isAdmin) {
                        return <Navigate to="/admin-dashboard" replace />;
                      } else {
                        return <Navigate to="/user-dashboard" replace />;
                      }
                    }}
                  />
                }
              />

              <Route
                path="/admin-dashboard"
                element={
                  <ProtectedRoute>
                    <AdminDashboard />
                  </ProtectedRoute>
                }
              />

              <Route path="*" element={<Navigate to="/login" replace />} />
            </Routes>
          </main>
        </div>
      </Router>
    </AuthProvider>
  );
}

// ProtectedRoute component
const ProtectedRoute = ({ children }) => {
  const { authState } = useAuthContext();

  if (!authState || !authState.token || !authState.user) {
    return <Navigate to="/login" replace />;
  }

  if (authState.user.role !== 'admin') {
    return <Navigate to="/login" replace />;
  }

  return children;
};

export default App;
