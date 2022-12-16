from __future__ import print_function

import os.path
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/admin.directory.user']


def main():
    """Add new user tp CyberSaint Google Workspace.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('admin', 'directory_v1', credentials=creds)

    firstName = input("First Name? ")
    lastName = input("Last Name? ")
    email = input("Email? ")
    address = input("Street address? Ex: 123 Main Street: ")
    city = input("City? ")
    state = input("State? Ex: LA: ")
    zipcode = input("Zip Code? ")
    phone = input("Phone number? Ex: 123 456 7890: ")

    newUser = {
        "primaryEmail": f"{firstName}.{lastName}@cybersaint.io",
        "name": {
            "familyName": f"{lastName}",
            "givenName": f"{firstName}",
            "displayName": f"{firstName} {lastName}",
            "fullName": f"{firstName} {lastName}"
        },
        "suspended": False,
        "password": "CyberStrong2023!",
        "changePasswordAtNextLogin": True,
        "emails": [
        {
        "address": f"{email}",
        "type": "home",
        "primary": True
        }
        ],
        "addresses": [
        {
        "type": "home",
        "streetAddress": f"{address}",
        "locality": f"{city}",
        "region": f"{state}",
        "postalCode": f"{zipcode}"
        }
        ],
        "phones": [
        {
        "value": f"+1 {phone}",
        "type": "work"
        }
        ],
        "includeInGlobalAddressList": True
        }

    # convert dict to json string
    # user_json = json.dumps(newUser)
    
    # Call the Admin SDK Directory API
    print('Adding new user to CyberSaint, Inc.')
    results = service.users().insert(body=newUser).execute()
    print("Added user: ", results)

if __name__ == '__main__':
    main()