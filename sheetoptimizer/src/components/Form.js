import React, { useState } from 'react';

function Form() {
  const [form1, setForm1] = useState({ name: '', signature: '' });
  const [form2, setForm2] = useState({ name: '', signature: '' });

  const handleForm1Change = (e) => {
    const { name, value } = e.target;
    setForm1((prevForm1) => ({
      ...prevForm1,
      [name]: value,
    }));
  };

  const handleForm2Change = (e) => {
    const { name, value } = e.target;
    setForm2((prevForm2) => ({
      ...prevForm2,
      [name]: value,
    }));
  };

  return (
    <div>
      {/* Form 1 */}
      <div>
        <h2>Signature</h2>
        <label>
          Name:
          <select
            name="name"
            value={form1.name}
            onChange={handleForm1Change}
          >
            <option value="">Select your name</option>
            <option value="John">John</option>
            <option value="Jane">Jane</option>
            <option value="Alex">Alex</option>
          </select>
        </label>
        <br />
        <label>
          Signature:
          <input
            type="text"
            name="signature"
            value={form1.signature}
            onChange={handleForm1Change}
          />
        </label>
      </div>

      {/* Form 2 */}
      <div>
        <h2>Merit</h2>
        <label>
          Name:
          <select
            name="name"
            value={form2.name}
            onChange={handleForm2Change}
          >
            <option value="">Select your name</option>
            <option value="John">John</option>
            <option value="Jane">Jane</option>
            <option value="Alex">Alex</option>
          </select>
        </label>
        <br />
        <label>
          # of points:
          <input
            type="text"
            name="signature"
            value={form2.signature}
            onChange={handleForm2Change}
          />
        </label>
      </div>
    </div>
  );
}

export default Form;
