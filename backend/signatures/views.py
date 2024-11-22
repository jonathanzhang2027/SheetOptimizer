from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Signature, MeritSheet
from .serializers import SignatureSerializer, MeritSheetSerializer
import gspread
from google.oauth2.service_account import Credentials
from google.oauth2 import id_token
from google.auth.transport import requests
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User
import os
from decouple import config
from django.conf import settings
import base64
from google.oauth2 import service_account
import json
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
# SERVICE_ACCOUNT_FILE = os.path.join(settings.BASE_DIR, 'credentials', 'service_account.json')

GOOGLE_CLIENT_ID = config('GOOGLE_CLIENT_ID')
SIGNATURE_FILE_NAME = config('SIGNATURE_FILE_NAME')
MERIT_FILE_NAME = config('MERIT_FILE_NAME')

service_account_json = base64.b64decode(os.getenv('GOOGLE_SERVICE_ACCOUNT')).decode('utf-8')

# Convert the decoded JSON to a dictionary
service_account_info = json.loads(service_account_json)

# Use the credentials to authenticate with Google Cloud services
credentials = service_account.Credentials.from_service_account_info(service_account_info)

# List of allowed emails
ALLOWED_EMAILS = config('ALLOWED_EMAILS', cast=lambda v: [s.strip() for s in v.split(',')])

class GoogleLoginView(APIView):
    def get(self, request):
        # Simple response to confirm the backend is working
        return Response("signatures")
    
    def post(self, request):
        token = request.data.get('token')

        if not token:
            raise AuthenticationFailed('Token is required.')

        try:
            # Verify the token using Google's library
            try:
                idinfo = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)
            except ValueError as e:
                raise AuthenticationFailed('Invalid token.')

            # Get user info
            email = idinfo['email']
            name = idinfo['name']

            # Check if the email is in the list of allowed emails
            if email not in ALLOWED_EMAILS:
                raise AuthenticationFailed('Unauthorized email.')

            # Check if user exists, otherwise create a new one
            user, _ = User.objects.get_or_create(username=email, defaults={"first_name": name})

            # Generate a session or token for the authenticated user
            return Response({"message": "Login successful", "email": email})

        except ValueError:
            raise AuthenticationFailed('Invalid token.')
from gspread.exceptions import WorksheetNotFound

from io import BytesIO
from googleapiclient.http import MediaIoBaseDownload, MediaIoBaseUpload

class SignatureView(APIView):
    def post(self, request):
        
        serializer = SignatureSerializer(data=request.data)
        # print(1)
        if serializer.is_valid():
            # print(1)
            serializer.save()
            # print(2)
            try:
                # Load credentials and initialize clients
                # print(1)
                # credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
                # print(1)
                drive_service = build('drive', 'v3', credentials=credentials)
                # print(1)
                gspread_client = gspread.authorize(credentials)
                # print(1)
                # Step 1: Find the `.xlsx` file in Google Drive
                # print(2)
                file_name = SIGNATURE_FILE_NAME  # Replace with the name of your file in Google Drive
                # print(2)
                query = f"name = '{file_name}' and mimeType = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' and trashed = false"
                print(1)
                results = drive_service.files().list(q=query, fields="files(id, name)").execute()
                files = results.get('files', [])
                print(file_name)
                print(files)
                
                if not files:
                    return Response({"error": f"No file named '{file_name}' found in Google Drive."}, status=404)
                # print(2)
                file_id = files[0]['id']
                print(f"Found file: {files[0]['name']} (ID: {file_id})")

                # Step 2: Convert the `.xlsx` file to a Google Sheet
                file_metadata = {'name': 'Converted Spreadsheet', 'mimeType': 'application/vnd.google-apps.spreadsheet'}
                converted_file = drive_service.files().copy(fileId=file_id, body=file_metadata).execute()
                spreadsheet_id = converted_file.get('id')
                print(f"Converted to Google Sheet with ID: {spreadsheet_id}")

                # Step 3: Open the Google Sheet and find the Active Name
                spreadsheet = gspread_client.open_by_key(spreadsheet_id)
                sheet = spreadsheet.sheet1  # Open the first worksheet
                rows = sheet.get_all_values()
                # print(1)
                # Find the Active Name and Update the Signature
                active_name = serializer.data['name']
                new_signature = serializer.data['signature']
                updated = False
                print(2)
                for i, row in enumerate(rows):
                    if row[0] == active_name:  # Assuming the Active Name is in the first column
                        print(f"Found Active Name at row {i + 1}")
                        sheet.update_cell(i + 1, 7, new_signature)  # Update the signature (column 7)
                        updated = True
                        break

                if not updated:
                    return Response({"error": f"Active Name '{active_name}' not found in the sheet."}, status=404)

                print("Signature updated successfully!")

                # Step 4: Export Google Sheet content and re-upload to Drive
                print("Exporting Google Sheet to .xlsx format...")
                request = drive_service.files().export_media(
                    fileId=spreadsheet_id,
                    mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
                file_stream = BytesIO()
                downloader = MediaIoBaseDownload(file_stream, request)
                done = False
                while not done:
                    status, done = downloader.next_chunk()
                    print(f"Export progress: {int(status.progress() * 100)}%")
                file_stream.seek(0)  # Reset stream pointer to the beginning

                # Step 5: Upload the .xlsx file back to Google Drive
                print("Uploading exported .xlsx back to Google Drive...")
                upload_metadata = {'name': {SIGNATURE_FILE_NAME}}  # Keep the same name
                media = MediaIoBaseUpload(file_stream, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                updated_file = drive_service.files().update(fileId=file_id, media_body=media, fields='id, name').execute()
                print(f"Updated file in Google Drive with ID: {updated_file['id']}")

                return Response({"message": "File processed and uploaded successfully.", "uploaded_file": updated_file})

            except Exception as e:
                return Response({"error": f"Unexpected error: {str(e)}"}, status=500)

        return Response(serializer.errors, status=400)

from googleapiclient.discovery import build
class MeritSheetView(APIView):
    def get(self, request):
        # Simple response to confirm the backend is working
        return Response("merit sheet")
    def post(self, request):
        serializer = MeritSheetSerializer(data=request.data)
        # print(1)
        if serializer.is_valid():
            serializer.save()
            # print(1)

            try:
                # Load credentials and initialize clients
                # credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
                drive_service = build('drive', 'v3', credentials=credentials)
                gspread_client = gspread.authorize(credentials)

                # Step 1: Find the `.xlsx` file in Google Drive
                file_name = MERIT_FILE_NAME  # Replace with the name of your file in Google Drive
                query = f"name = '{file_name}' and mimeType = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' and trashed = false"
                results = drive_service.files().list(q=query, fields="files(id, name)").execute()
                files = results.get('files', [])

                if not files:
                    return Response({"error": f"No file named '{file_name}' found in Google Drive."}, status=404)

                file_id = files[0]['id']
                print(f"Found file: {files[0]['name']} (ID: {file_id})")

                # Step 2: Convert the `.xlsx` file to a Google Sheet
                file_metadata = {'name': 'Converted Spreadsheet', 'mimeType': 'application/vnd.google-apps.spreadsheet'}
                converted_file = drive_service.files().copy(fileId=file_id, body=file_metadata).execute()
                spreadsheet_id = converted_file.get('id')
                print(f"Converted to Google Sheet with ID: {spreadsheet_id}")

                # Step 3: Open the Google Sheet and append a new row
                spreadsheet = gspread_client.open_by_key(spreadsheet_id)
                sheet = spreadsheet.sheet1  # Open the first worksheet
                # print(1)
                
                points_value = serializer.data.get('points', 0)
                try:
                    points_value = int(points_value)
                except ValueError:
                    points_value = ''  # Default to 0 if the conversion fails
                    
                date = serializer.data.get('date', ''),
                new_date = ''
                if isinstance(date, tuple):
                    date = date[0]  # Get the first element of the tuple, which is the date string
                
                # Now check if date is not empty
                if date != '':
                    print(date)  # This should print '2024-10-31' as a string
                    
                    # Format the date
                    new_date = date[5:7] + '/' + date[8:10] + '/' + date[0:4]
                
                # Create the new_row
                new_row = [
                    new_date,
                    serializer.data.get('active_name', ''),
                    serializer.data.get('professional', ''),
                    serializer.data.get('brotherhood', ''),
                    serializer.data.get('initial', ''),
                    points_value,
                ]            
                                # print(1)
                
                sheet.append_row(new_row)
                print(f"Appended new row: {new_row}")

                # Step 4: Export Google Sheet content and re-upload to Drive
                print("Exporting Google Sheet to .xlsx format...")
                request = drive_service.files().export_media(
                    fileId=spreadsheet_id,
                    mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
                file_stream = BytesIO()
                downloader = MediaIoBaseDownload(file_stream, request)
                done = False
                while not done:
                    status, done = downloader.next_chunk()
                    print(f"Export progress: {int(status.progress() * 100)}%")
                file_stream.seek(0)  # Reset stream pointer to the beginning

                # Step 5: Upload the `.xlsx` file back to Google Drive
                print("Uploading exported .xlsx back to Google Drive...")
                upload_metadata = {'name': MERIT_FILE_NAME}  # Keep the same name
                media = MediaIoBaseUpload(file_stream, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                updated_file = drive_service.files().update(fileId=file_id, media_body=media, fields='id, name').execute()
                print(f"Updated file in Google Drive with ID: {updated_file['id']}")

                return Response({"message": "Merit sheet processed and uploaded successfully.", "uploaded_file": updated_file})

            except Exception as e:
                return Response({"error": f"Unexpected error: {str(e)}"}, status=500)

        return Response(serializer.errors, status=400)

