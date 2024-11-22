# Passion Project: Signature and Merit Sheet Streamlining Tool

## Description

This project aims to streamline the process of inserting signatures and merit sheets into spreadsheets through an intuitive, user-friendly interface. The tool simplifies manual data entry, reduces input errors, and enhances workflow efficiency by incorporating dynamic dropdowns, signature input fields, and user authentication. It is optimized for low-connectivity environments, ensuring usability even when internet speeds are slower.

### Key Features
- **Dynamic Dropdown Menu**: Allows users to type and filter names in real-time for fast selection.
- **Signature Input Box**: Lets users insert signatures corresponding to active members.
- **User Authentication**: OAuth-based authentication to ensure only authorized users can input data.
- **Optimized for Low Connectivity**: Minimized reliance on high-speed internet for better accessibility.

## Technologies Used
- **Frontend**: React.js, OAuth
- **Backend**: Python, Pandas for data manipulation, Django for API handling
- **Authentication**: OAuth (Google OAuth)
- **Deployment**: Vercel (Frontend and Backend deployed separately)
- **Database**: SQLite (for backend development and testing)

## Installation

### Prerequisites

1. **Frontend** (React.js):
    - Node.js (v16+)
    - NPM (v8+)
    
2. **Backend** (Django):
    - Python 3.8+
    - Django 4.x
    - Pandas 1.x
    
3. **Authentication**:
    - Google OAuth credentials (Client ID, Secret) from Google Cloud Console

### Steps to Run Locally

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/signature-merit-tool.git
    cd signature-merit-tool
    ```

2. **Frontend Setup**:
    - Navigate to the `frontend` directory.
    - Install the required packages:
        ```bash
        npm install
        ```
    - Create a `.env` file in the root of the frontend directory and add the following:
        ```bash
        REACT_APP_GOOGLE_CLIENT_ID=your-google-client-id
        REACT_APP_API_URL=http://localhost:8000/api
        ```

3. **Backend Setup**:
    - Navigate to the `backend` directory.
    - Create and activate a virtual environment:
        ```bash
        python3 -m venv venv
        source venv/bin/activate   # On Windows, use venv\Scripts\activate
        ```
    - Install the required dependencies:
        ```bash
        pip install -r requirements.txt
        ```
    - Set up environment variables (`GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, `GOOGLE_REDIRECT_URI`, etc.)
    - Run the backend server:
        ```bash
        python manage.py runserver
        ```

4. **Run the Frontend**:
    - In the `frontend` directory, start the React development server:
        ```bash
        npm start
        ```

### Notes:
- The backend will be available at `http://localhost:8000/` by default.
- The frontend will be available at `http://localhost:3000/`.

## Use Case

### Problem:
The manual process of inserting signatures and merit sheets into spreadsheets is time-consuming, error-prone, and inefficient. This process often requires individuals to manually type and manage data, leading to mistakes and slower workflows.

### Solution:
This project provides a **web application** with the following key components:
1. **Dropdown for Member Selection**: A dynamic dropdown allows users to search and select names from a list of active members.
2. **Signature Input**: A simple input box allows users to sign directly, ensuring signatures correspond to the correct members.
3. **User Authentication**: OAuth authentication ensures that only authorized users can access and input data into the system.
4. **Automated Data Management**: The backend automatically processes and updates Google Sheets using Google APIs, ensuring seamless data flow and accuracy.

### Target Users:
- **Organizations** needing a streamlined way to handle signatures and merit sheets.
- **Admin/Staff** responsible for organizing and collecting signatures and other merit-related data.
- **Users in Low-Connectivity Environments** where the tool needs to be lightweight and optimized for efficiency.

### Key Benefits:
- **Increased Efficiency**: Reduces manual data entry time, automating tasks related to signatures and merit sheets.
- **User-Friendly Interface**: Easy-to-use, even for those with limited technical experience.
- **Reduced Errors**: Automates data entry, decreasing the likelihood of human error.
- **Access Control**: Only authorized users can input or modify data through OAuth integration.

## Future Enhancements
- **Expanded Authentication Support**: Adding support for other OAuth providers (Facebook, GitHub, etc.).
- **Mobile App**: Developing a mobile version of the app for ease of use on the go.
- **Integration with Other Tools**: Expanding integration to include more data sources like Google Forms or spreadsheets beyond just signatures.

## Contributing
We welcome contributions! If you’d like to improve the project or add new features, feel free to fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you’d like to change.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Contact
For any questions or feedback, feel free to reach out to me at: **your-email@example.com**.

---

This README format gives a clear structure for the project, ensuring that anyone who comes across your repository will know what the project is about, how to run it locally, and the value it provides. It also includes helpful sections like contributing guidelines and future enhancements to encourage community involvement.
