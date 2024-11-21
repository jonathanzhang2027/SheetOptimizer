// import React, { useState } from 'react';
import Select from 'react-select';

const DynamicDropdown = ({ options, onChange }) => {
  return (
    <Select
      options={options.map((opt) => ({ label: opt, value: opt }))}
      onChange={(selected) => onChange(selected.value)}
      isSearchable
      placeholder="Select or type to search..."
    />
  );
};

export default DynamicDropdown;
