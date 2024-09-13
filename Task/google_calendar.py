import os
import pickle
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']

def iniciarGoogleCalendar():
    credenciais = None

    if os.path.exists("token.pickle"):
        with open('token.pickle', 'rb') as token:
            credenciais = pickle.load(token)

    if not credenciais or not credenciais.valid:
        if credenciais and credenciais.expired and credenciais.refresh_token:
            try:
                credenciais.refresh(Request())
            
            except Exception as e:
                print(f"Erro ao atualizar as credenciais: {e}")
                credenciais = None
        
        if not credenciais or not credenciais.valid:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            credenciais = flow.run_local_server(port=0)

            with open('token.pickle', 'wb') as token:
                pickle.dump(credenciais, token)
        
    servico = build('calendar', 'v3', credentials=credenciais)
    return servico
