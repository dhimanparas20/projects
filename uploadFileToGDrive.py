###########################################

#WARNING : dont use firefox, only Chrome

#######################################3
import os
import pickle
import requests
import collections
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from requests.exceptions import JSONDecodeError
from tqdm import tqdm
import requests_toolbelt

cwd = os.getcwd()

def authenticate():
    """Authenticate the user and return the access token"""
    SCOPES = ['https://www.googleapis.com/auth/drive.file']
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secrets.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    return creds.token

class ProgressBar(tqdm):
    def update_to(self, n: int) -> None:
        self.update(n - self.n)

def upload_file(access_token: str, file_name: str, file_path: str, parent_folder_id: str = None):
    metadata = {
        "name": file_name,
    }

    if parent_folder_id:
        metadata["parents"] = [parent_folder_id]

    files = {}
    session = requests.session()

    with open(file_path, "rb") as fp:
        files = collections.OrderedDict(data=("metadata", json.dumps(metadata), "application/json"), file=fp)

        encoder = requests_toolbelt.MultipartEncoder(files)
        with ProgressBar(
            total=encoder.len,
            unit="B",
            unit_scale=True,
            unit_divisor=1024,
            miniters=1,
        ) as bar:
            monitor = requests_toolbelt.MultipartEncoderMonitor(
                encoder, lambda monitor: bar.update_to(monitor.bytes_read)
            )

            r = session.post(
                "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
                data=monitor,
                allow_redirects=False,
                headers={
                    "Authorization": "Bearer " + access_token,
                    "Content-Type": monitor.content_type,
                },
            )

    try:
        resp = r.json()
        print(resp)
    except JSONDecodeError:
        sys.exit(r.text)

# Authenticate and upload the file
access_token = authenticate()
folder_id = "1H-GF8U3YaKR2SR-lTMEFnTPBq_1E3upS"
file_name = "Dark Shadows (2012) (1080p BluRay x265 10bit Tigole).mkv"
file_path = os.path.join(cwd, file_name)

upload_file(access_token, file_name, file_path, parent_folder_id=folder_id)
