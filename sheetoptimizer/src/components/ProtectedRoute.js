import React from 'react';
import { Navigate } from 'react-router-dom';

const ProtectedRoute = ({ children }) => {
  // Check if a valid token exists (indicating successful OAuth login)
  const isAuthenticated = localStorage.getItem('token'); // Assuming the token is stored in localStorage

  // If not authenticated, redirect to the login page
  if (!isAuthenticated) {
    return <Navigate to="/" />;
  }

  // If authenticated, render the protected component
  return children;
};

export default ProtectedRoute;
