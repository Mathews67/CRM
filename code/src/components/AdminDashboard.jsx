import React from "react";
import { Link } from "react-router-dom";

// Sample data for analysis, can be fetched from API
const sampleData = {
  users: 120,
  crimeCategories: 15,
  crimes: 350,
  policeStations: 5,
  officers: 50,
  evidence: 100,
  criminalRecords: 75,
  reportingOfficers: 10,
  courts: 3,
  courtCases: 45,
  witnesses: 30
};

const AdminDashboard = () => {
  return (
    <div className="dashboard-container">
      {/* Sidebar */}
      <div className="sidebar">
        <h2>Admin Dashboard</h2>
        <ul>
          <li>
            <Link to="/dashboard">Dashboard</Link>
          </li>
          <li>
            <Link to="/users">Users</Link>
          </li>
          <li>
            <Link to="/crime-categories">Crime Categories</Link>
          </li>
          <li>
            <Link to="/crimes">Crimes</Link>
          </li>
          <li>
            <Link to="/police-stations">Police Stations</Link>
          </li>
          <li>
            <Link to="/officers">Officers</Link>
          </li>
          <li>
            <Link to="/evidence">Evidence</Link>
          </li>
          <li>
            <Link to="/criminal-records">Criminal Records</Link>
          </li>
          <li>
            <Link to="/reporting-officers">Reporting Officers</Link>
          </li>
          <li>
            <Link to="/courts">Courts</Link>
          </li>
          <li>
            <Link to="/court-cases">Court Cases</Link>
          </li>
          <li>
            <Link to="/witnesses">Witnesses</Link>
          </li>
        </ul>
      </div>

      {/* Main Content */}
      <div className="main-content">
        <h1>Welcome to the Admin Dashboard</h1>
        
        <div className="cards-container">
          {/* Users Card */}
          <div className="card">
            <h3>Total Users</h3>
            <p>{sampleData.users} users</p>
            <p>Admin can manage all users here, including assigning roles and editing details.</p>
          </div>

          {/* Crime Categories Card */}
          <div className="card">
            <h3>Total Crime Categories</h3>
            <p>{sampleData.crimeCategories} categories</p>
            <p>Admin can add, edit, and delete crime categories to classify crimes effectively.</p>
          </div>

          {/* Crimes Card */}
          <div className="card">
            <h3>Total Crimes</h3>
            <p>{sampleData.crimes} crimes</p>
            <p>Admin can monitor and manage all crime reports in the system.</p>
          </div>

          {/* Police Stations Card */}
          <div className="card">
            <h3>Total Police Stations</h3>
            <p>{sampleData.policeStations} stations</p>
            <p>Admin can add and edit police stations as required in the system.</p>
          </div>

          {/* Officers Card */}
          <div className="card">
            <h3>Total Officers</h3>
            <p>{sampleData.officers} officers</p>
            <p>Admin can manage officer profiles and their roles within the system.</p>
          </div>

          {/* Evidence Card */}
          <div className="card">
            <h3>Total Evidence Items</h3>
            <p>{sampleData.evidence} pieces of evidence</p>
            <p>Admin can oversee evidence collection and management linked to crimes.</p>
          </div>

          {/* Criminal Records Card */}
          <div className="card">
            <h3>Total Criminal Records</h3>
            <p>{sampleData.criminalRecords} records</p>
            <p>Admin can monitor and update criminal records within the system.</p>
          </div>

          {/* Reporting Officers Card */}
          <div className="card">
            <h3>Total Reporting Officers</h3>
            <p>{sampleData.reportingOfficers} officers</p>
            <p>Admin can manage reporting officers and assign cases to them.</p>
          </div>

          {/* Courts Card */}
          <div className="card">
            <h3>Total Courts</h3>
            <p>{sampleData.courts} courts</p>
            <p>Admin can add and edit court details for case processing.</p>
          </div>

          {/* Court Cases Card */}
          <div className="card">
            <h3>Total Court Cases</h3>
            <p>{sampleData.courtCases} cases</p>
            <p>Admin can monitor and manage ongoing court cases.</p>
          </div>

          {/* Witnesses Card */}
          <div className="card">
            <h3>Total Witnesses</h3>
            <p>{sampleData.witnesses} witnesses</p>
            <p>Admin can view and manage witness profiles within the system.</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AdminDashboard;
