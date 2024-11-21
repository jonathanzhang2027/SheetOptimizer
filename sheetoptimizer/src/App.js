import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './components/Login';
import ProtectedRoute from './components/ProtectedRoute';
import SignatureAndMeritForm from './components/SignatureAndMeritForm';
// import GoogleDriveProcessor from './components/GoogleDriveProcessor';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <SignatureAndMeritForm />
            </ProtectedRoute>
          }
        />
      </Routes>
    </Router>
  );
};

export default App;
