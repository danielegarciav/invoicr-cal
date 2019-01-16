import os.path
import datetime
from httplib2 import Http 
from googleapiclient.discovery import build
from oauth2client import file, client, tools

GCAL_CREDS_FOLDER = "gcal_credentials"
TOKEN_FILE = os.path.join(GCAL_CREDS_FOLDER, "token.json")
CRED_FILE = os.path.join(GCAL_CREDS_FOLDER, "credentials.json")

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'


class GCalWrapper():
    def __init__(self):
        if not os.path.isfile(CRED_FILE):
            raise(FileNotFoundError("{} was not found".format(TOKEN_FILE)))

        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        self.store = file.Storage(TOKEN_FILE)
        self.creds = self.store.get()
        if not self.creds or self.creds.invalid:
            self.flow = client.flow_from_clientsecrets(CRED_FILE, SCOPES)
            self.creds = tools.run_flow(self.flow, self.store)
        self.service = build('calendar', 'v3', http=self.creds.authorize(Http()))