import React from "react";
import { Link } from "react-router-dom";
import "../styles/AdminDashboard.css";

const AdminDashboard = () => {
  return (
    <div className="dashboard-container">
      {/* Sidebar */}
      <div className="sidebar">
    
        <ul>
          <li><Link to="/dashboard" className="sidebar-link">CRM-Dashboard</Link></li>
          <li><Link to="/users" className="sidebar-link">Users</Link></li>
          <li><Link to="/crime-categories" className="sidebar-link">Crime Categories</Link></li>
          <li><Link to="router.register(r'crime-categories', views.CrimeCategoryViewSet)" className="sidebar-link">Crimes</Link></li>
          <li><Link to="/police-stations" className="sidebar-link">Police Stations</Link></li>
          <li><Link to="/officers" className="sidebar-link">Officers</Link></li>
          <li><Link to="/evidence" className="sidebar-link">Evidence</Link></li>
          <li><Link to="/criminal-records" className="sidebar-link">Criminal Records</Link></li>
          <li><Link to="/reporting-officers" className="sidebar-link">Reporting Officers</Link></li>
          <li><Link to="/courts" className="sidebar-link">Courts</Link></li>
          <li><Link to="/court-cases" className="sidebar-link">Court Cases</Link></li>
          <li><Link to="/witnesses" className="sidebar-link">Witnesses</Link></li>
        </ul>
      </div>

      {/* Main Content */}
      <div className="main-content">
        <h1 className="main-title">Welcome to the Admin Dashboard</h1>

        <div className="cards-container">
          {/* Dashboard Card */}
          <div className="card">
            <h3>Dashboard</h3>
            <p>Overview of the system</p>
          </div>

          {/* Users Card */}
          <div className="card">
            <h3>Total Users</h3>
            <p>120 users</p>
          </div>

          {/* Crime Categories Card */}
          <div className="card">
            <h3>Total Crime Categories</h3>
            <p>15 categories</p>
          </div>

          {/* Crimes Card */}
          <div className="card">
            <h3>Total Crimes</h3>
            <p>350 crimes</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AdminDashboard;
