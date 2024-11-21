import React from 'react';
import { GoogleOAuthProvider, GoogleLogin } from '@react-oauth/google';
import axios from 'axios';
import { useNavigate } from 'react-router-dom'; // Import useNavigate

const Login = () => {
  const clientId = process.env.REACT_APP_GOOGLE_CLIENT_ID; // Access the Client ID from .env
  const navigate = useNavigate();

  const handleLoginSuccess = async (response) => {
    console.log('Google Login Success:', response);
    // console.log('Google Login Success Response:', response); // Debugging
    console.log('Token:', response.credential); // Debugging
    try {
      const res = await axios.post('http://localhost:8000/api/google-login/', {
        token: response.credential,
      });
      localStorage.setItem('token', res.data.token); // Save the token
      console.log('Login successful!');
      navigate('/dashboard');
    } catch (error) {
      console.error('Login Failed:', error);
    }
  };

  const handleLoginFailure = (response) => {
    console.error('Google Login Failed:', response);
  };

  return (
    <GoogleOAuthProvider clientId={clientId}>
      <div>
        <h1>Login with Google</h1>
        <GoogleLogin onSuccess={handleLoginSuccess} onError={handleLoginFailure} scope="https://www.googleapis.com/auth/drive https://www.googleapis.com/auth/drive.file" />
      </div>
    </GoogleOAuthProvider>
  );
};

export default Login;
