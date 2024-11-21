from flask import Flask, request, jsonify
import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

# Initialize Flask app
app = Flask(__name__)

# Google Sheets setup
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("path/to/credentials.json", scopes=SCOPES)
client = gspread.authorize(creds)

# Access Google Sheet
SPREADSHEET_ID = "your_spreadsheet_id_here"
sheet = client.open_by_key(SPREADSHEET_ID).sheet1  # Access the first sheet

# Function to read Google Sheet into a DataFrame
def read_sheet():
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    return df

# Route to get member names for dropdown
@app.route('/get_members', methods=['GET'])
def get_members():
    df = read_sheet()
    # Assuming 'Name' is a column in the sheet with member names
    members = df['Name'].tolist()
    return jsonify(members)

# Route to add signature for a member
@app.route('/add_signature', methods=['POST'])
def add_signature():
    data = request.json
    member_name = data.get('member_name')
    signature = data.get('signature')

    # Read the sheet into a DataFrame
    df = read_sheet()

    # Update signature for the specified member
    if member_name in df['Name'].values:
        df.loc[df['Name'] == member_name, 'Signature'] = signature
        # Write DataFrame back to Google Sheet
        sheet.update([df.columns.values.tolist()] + df.values.tolist())
        return jsonify({"status": "success", "message": "Signature updated"})
    else:
        return jsonify({"status": "error", "message": "Member not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
