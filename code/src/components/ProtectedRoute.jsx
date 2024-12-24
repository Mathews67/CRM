import React from 'react';
import { Navigate } from 'react-router-dom';
import { useAuthContext } from '../context/AuthContext';

const ProtectedRoute = ({ children, role }) => {
  const { authState } = useAuthContext();

  // Redirect to login if not authenticated
  if (!authState || !authState.token || !authState.user) {
    return <Navigate to="/login" replace />;
  }

  // Check user role and redirect appropriately
  if (role && authState.user.role !== role) {
    return <Navigate to="/unauthorized" replace />;
  }

  return children;
};

export default ProtectedRoute;
