import React, { useState } from 'react';
import axios from 'axios';
import DynamicDropdown from './DynamicDropdown';

const SignatureAndMeritForm = () => {
  const [signatureForm, setSignatureForm] = useState({ name: '', signature: '' });
  const [meritForm, setMeritForm] = useState({
    active_name: '',
    professional: '',
    brotherhood: '',
    initial: '',
    points: '',
  });
  const names = ['Amber Yeh', 'Jane', 'Alex', 'Alice'];

  // Get token from localStorage
  const getAuthHeader = () => {
    const token = localStorage.getItem('token');
    return token ? { Authorization: `Bearer ${token}` } : {};
  };

  const handleSignatureSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post(
        'http://localhost:8000/api/signature/',
        signatureForm,
        { headers: getAuthHeader() }
      );
      alert('Signature submitted!');
    } catch (error) {
      console.error('Failed to submit signature:', error);
      alert('Failed to submit signature. Please try again.');
    }
  };

  const handleMeritSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post(
        'http://localhost:8000/api/merit-sheet/',
        meritForm,
        { headers: getAuthHeader() }
      );
      alert('Merit sheet submitted!');
    } catch (error) {
      console.error('Failed to submit merit sheet:', error);
      alert('Failed to submit merit sheet. Please try again.');
    }
  };

  return (
    <div>
      <h1>Signature and Merit Forms</h1>

      {/* Signature Form */}
      <form onSubmit={handleSignatureSubmit}>
        <h2>Signature</h2>
        <DynamicDropdown
          options={names}
          onChange={(value) => setSignatureForm({ ...signatureForm, name: value })}
        />
        <input
          type="text"
          placeholder="Signature"
          value={signatureForm.signature}
          onChange={(e) => setSignatureForm({ ...signatureForm, signature: e.target.value })}
        />
        <button type="submit">Submit Signature</button>
      </form>

      {/* Merit Form */}
      <form onSubmit={handleMeritSubmit}>
        <h2>Merit</h2>
        <DynamicDropdown
          options={names}
          onChange={(value) => setMeritForm({ ...meritForm, active_name: value })}
        />
        <input
          type="text"
          placeholder="Professional"
          value={meritForm.professional}
          onChange={(e) => setMeritForm({ ...meritForm, professional: e.target.value })}
        />
        <input
          type="text"
          placeholder="Brotherhood"
          value={meritForm.brotherhood}
          onChange={(e) => setMeritForm({ ...meritForm, brotherhood: e.target.value })}
        />
        <input
          type="text"
          placeholder="Initial"
          value={meritForm.initial}
          onChange={(e) => setMeritForm({ ...meritForm, initial: e.target.value })}
        />
        <input
          type="text"
          placeholder="Points"
          value={meritForm.points}
          onChange={(e) => setMeritForm({ ...meritForm, points: e.target.value })}
        />
        <button type="submit">Submit Merit</button>
      </form>
    </div>
  );
};

export default SignatureAndMeritForm;
