import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import Login from './components/Login';
import ProtectedRoute from './components/ProtectedRoute';
import AdminDashboard from './components/AdminDashboard';
import Crime from './components/Crime';
import PoliceStation from './components/PoliceStation';
import Witness from './components/Witness';
import CourtCase from './components/CourtCase';
import Officer from './components/Officer';
import ReportingOfficer from './components/ReportingOfficer';
import CrimeCategory from './components/CrimeCategory';
import Complaints from './components/Complaints';
import './App.css';

function App() {
  return (
    <AuthProvider>
      <Router>
        <div className="App">
          <main className="container mx-auto px-4">
            <Routes>
              <Route
                path="/login"
                element={<Login />}
              />

              <Route
                path="/AdminDashboard"
                element={
                  <ProtectedRoute>
                    <AdminDashboard />
                  </ProtectedRoute>
                }
              />

              {/* Define routes for the other components */}
              <Route
                path="/crimes"
                element={
                  <ProtectedRoute>
                    <Crime />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/police-stations"
                element={
                  <ProtectedRoute>
                    <PoliceStation />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/witnesses"
                element={
                  <ProtectedRoute>
                    <Witness />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/court-cases"
                element={
                  <ProtectedRoute>
                    <CourtCase />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/officers"
                element={
                  <ProtectedRoute>
                    <Officer />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/reporting-officers"
                element={
                  <ProtectedRoute>
                    <ReportingOfficer />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/crime-categories"
                element={
                  <ProtectedRoute>
                    <CrimeCategory />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/complaints"
                element={
                  <ProtectedRoute>
                    <Complaints />
                  </ProtectedRoute>
                }
              />

              {/* Redirect any unknown routes to login */}
              <Route path="*" element={<Navigate to="/login" replace />} />
            </Routes>
          </main>
        </div>
      </Router>
    </AuthProvider>
  );
}

export default App;
