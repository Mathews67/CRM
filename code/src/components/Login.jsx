import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuthContext } from '../context/AuthContext';
import '../styles/Login.css';

const Login = () => {
  const [formState, setFormState] = useState({
    username: '',
    password: '',
  });
  const [isLoading, setIsLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState('');
  const { loginUser, user } = useAuthContext();
  const navigate = useNavigate();

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormState((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleLogin = async (event) => {
    event.preventDefault();
    setIsLoading(true);
    setErrorMessage('');

    const { username, password } = formState;

    if (!username || !password) {
      setErrorMessage('Please enter both username and password.');
      setIsLoading(false);
      return;
    }

    try {
      const response = await fetch('http://localhost:8000/api/login/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || 'Invalid credentials.');
      }

      const { access, user } = data;

      loginUser(access, user);

      if (user.role === 'Admin') {
        navigate('/AdminDashboard');
      } else {
        navigate('/userDashboard');
      }
    } catch (error) {
      setErrorMessage(error.message || 'An error occurred. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    if (user) {
      // Optionally handle something after the user is logged in
    }
  }, [user]);

  return (
    <div className="login-container">
      <div className="login-card">
        
        {errorMessage && (
          <div className="error-message">
            <span>{errorMessage}</span>
          </div>
        )}

        <form onSubmit={handleLogin} className="login-form">
          <div className="form-group">
            <div className="input-wrapper">
              <i className="icon fa fa-user"></i>
              <input
                type="text"
                name="username"
                placeholder="Username"
                value={formState.username}
                onChange={handleInputChange}
                required
              />
            </div>
          </div>

          <div className="form-group">
            <div className="input-wrapper">
              <i className="icon fa fa-lock"></i>
              <input
                type="password"
                name="password"
                placeholder="Password"
                value={formState.password}
                onChange={handleInputChange}
                required
              />
            </div>
          </div>

          <button
            type="submit"
            disabled={isLoading}
            className={`login-button ${isLoading ? 'loading' : ''}`}
          >
            {isLoading ? 'Signing in...' : 'Login'}
          </button>
        </form>

        <div className="login-footer">
          <p>
            Don't have an account?{' '}
            <button
              onClick={() => navigate('/register')}
              className="register-link"
            >
              Sign up here
            </button>
          </p>
        </div>
      </div>

      {user && (
        <div className="user-info">
          <span className="user-icon">&#128100;</span>
          <span>{user.username}</span>
        </div>
      )}
    </div>
  );
};

export default Login;
