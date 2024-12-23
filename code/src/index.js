import React from "react";
import ReactDOM from "react-dom/client";  // Import the 'client' version of ReactDOM
import App from "./App";
import { AuthProvider } from "./context/AuthContext";  // Import AuthProvider

// Create root element using React 18's createRoot
const root = ReactDOM.createRoot(document.getElementById("root"));

// Render the App wrapped with AuthProvider
root.render(
  <AuthProvider>
    <App />
  </AuthProvider>
);
