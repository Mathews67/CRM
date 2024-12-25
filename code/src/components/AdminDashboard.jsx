import React from "react";
import { useState,useEffect } from "react";
import { Link } from "react-router-dom";
import "../styles/AdminDashboard.css";
import { useAuthContext } from '../context/AuthContext';
import { 
    FaHome,
    FaUsers,
    FaBuilding, 
    FaUserShield, 
    FaAddressBook, 
    FaBook, 
    FaLock,
    FaBriefcase,
    FaUserFriends, 
    FaClipboardList,
    FaUserCircle 
    } from 'react-icons/fa';


const AdminDashboard = () => {
  const { authState } = useAuthContext(); 
  const [adminUsername, setAdminUsername] = useState('');

  useEffect(() => {
    if (authState.user) {
      setAdminUsername(authState.user.username || 'Admin'); 
    }
  }, [authState.user]);
  return (
    <div className="dashboard-container">
  {/* Sidebar */}
  <div className="sidebar">
    <ul className="sidebar-list">
      <li>
        <Link to="/dashboard" className="sidebar-link">
          <FaHome className="sidebar-icon" /> CRM-Dashboard
        </Link>
      </li>
      <li>
        <Link to="/users" className="sidebar-link">
          <FaUsers className="sidebar-icon" /> Users
        </Link>
      </li>
      <li>
        <Link to="/PoliceStation" className="sidebar-link">
          <FaBuilding className="sidebar-icon" /> Police Stations
        </Link>
      </li>
      <li>
        <Link to="/Officer" className="sidebar-link">
          <FaUserShield className="sidebar-icon" /> Officers
        </Link>
      </li>
      <li>
        <Link to="/ReportingOfficer" className="sidebar-link">
          <FaAddressBook className="sidebar-icon" /> Reporting Officers
        </Link>
      </li>
      <li>
        <Link to="/CrimeCategory" className="sidebar-link">
          <FaBook className="sidebar-icon" /> Crime Categories
        </Link>
      </li>
      <li>
        <Link to="/Crime" className="sidebar-link">
          <FaLock className="sidebar-icon" /> Crimes
        </Link>
      </li>
      <li>
        <Link to="/CourtCase" className="sidebar-link">
          <FaBriefcase className="sidebar-icon" /> Court Cases
        </Link>
      </li>
      <li>
        <Link to="/Witness" className="sidebar-link">
          <FaUserFriends className="sidebar-icon" /> Witnesses
        </Link>
      </li>
      <li>
        <Link to="/Complaints" className="sidebar-link">
          <FaClipboardList className="sidebar-icon" /> Complaints
        </Link>
      </li>
    </ul>
  </div>

  {/* Main Content */}
  <div className="main-content">
    {/* Top Right User Account */}
    <div className="top-right">
      <FaUserCircle className="user-icon" />
      <span className="username">{adminUsername}</span>
    </div>

    <h1 className="main-title">Welcome to the Admin Dashboard</h1>

    <div className="cards-container">
      {/* Dashboard Card */}
      <div className="card">
        <FaHome className="card-icon" />
        <h3>Dashboard</h3>
        <p>Overview of the system</p>
      </div>

      {/* Users Card */}
      <div className="card">
        <FaUsers className="card-icon" />
        <h3>Total Users</h3>
        <p>120 users</p>
      </div>

      {/* Crime Categories Card */}
      <div className="card">
        <FaBook className="card-icon" />
        <h3>Total Crime Categories</h3>
        <p>15 categories</p>
      </div>

      {/* Crimes Card */}
      <div className="card">
        <FaLock className="card-icon" />
        <h3>Total Crimes</h3>
        <p>350 crimes</p>
      </div>
    </div>
  </div>
</div>
  )
};

export default AdminDashboard;
