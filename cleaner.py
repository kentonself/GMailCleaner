import os.path
import sys

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]

delete = False
queries = [
    "from:\"heather cox richardson\" older_than:10d", # Heather Cox Richardson
    "from:uspsinformeddelivery older_than:30d"    #USPS informed delivery
]

def main():
  """Shows basic usage of the Gmail API.
  Lists the user's Gmail labels.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  for query in queries:
      try:
        # Call the Gmail API
        service = build("gmail", "v1", credentials=creds)
        results = service.users().threads().list(userId="me",q=query ).execute()
        messages = results.get("threads", [])
    
        if not messages:
          print("No results found.")
          continue
        print("Labels:")
        for message in messages:
          print(message)
          if delete:
            print(f"deleting: {message['id']}, {message['snippet']}")
            results = service.users().threads().trash(userId= "me", id=message["id"]).execute()
            sys.exit()
    
      except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f"An error occurred: {error}")
    

if __name__ == "__main__":
  main()