import React, { useState } from "react";
import axios from "axios";

const GoogleDriveProcessor = () => {
  const [folderId, setFolderId] = useState("");
  const [signatureData, setSignatureData] = useState({ signature: "", names: [] });
  const [meritData, setMeritData] = useState({ date: "", fields: [] });
//   const [authUrl, setAuthUrl] = useState(null);
  const [response, setResponse] = useState(null);

//   const handleOAuthInit = async () => {
//     try {
//       const res = await axios.get("http://127.0.0.1:8000/api/oauth-init/");
//       setAuthUrl(res.data.auth_url);
//     } catch (error) {
//       console.error("Error initializing OAuth:", error);
//     }
//   };

  const handleProcessFolder = async () => {
    try {
      const res = await axios.post("http://127.0.0.1:8000/api/process-folder/", {
        folder_id: folderId,
        signature_data: signatureData,
        merit_data: meritData,
      });
      setResponse(res.data);
    } catch (error) {
      console.error("Error processing folder:", error);
    }
  };

  return (
    <div>
      <h1>Google Drive Processor</h1>
      <input
        type="text"
        placeholder="Enter Folder ID"
        value={folderId}
        onChange={(e) => setFolderId(e.target.value)}
      />
      <h2>Signature Data</h2>
      <input
        type="text"
        placeholder="Signature"
        value={signatureData.signature}
        onChange={(e) =>
          setSignatureData({ ...signatureData, signature: e.target.value })
        }
      />
      <input
        type="text"
        placeholder="Names (comma-separated)"
        onChange={(e) =>
          setSignatureData({
            ...signatureData,
            names: e.target.value.split(","),
          })
        }
      />
            <h2>Merit Data</h2>
      <input
        type="text"
        placeholder="Date"
        value={meritData.date}
        onChange={(e) => setMeritData({ ...meritData, date: e.target.value })}
      />
      <input
        type="text"
        placeholder="Fields (comma-separated)"
        onChange={(e) =>
          setMeritData({ ...meritData, fields: e.target.value.split(",") })
        }
      />
      <button onClick={handleProcessFolder}>Process Folder</button>
      {response && (
        <div>
          <h3>{response.message}</h3>
          <ul>
            {response.modified_files.map((file, index) => (
              <li key={index}>{file.name}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default GoogleDriveProcessor;

