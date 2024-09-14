import os
import pickle
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar']

def iniciar_google_calendar():
    
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
        else:

            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            credenciais = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(credenciais, token)

    
    servico = build('calendar', 'v3', credentials=credenciais)
    return servico

def criar_evento(service, resumo, descricao, data_inicio, data_fim):

    evento = {
        'summary': resumo,
        'description': descricao,
        'start': {
            'dateTime': data_inicio,
            'timeZone': 'America/Sao_Paulo',
        },
        'end': {
            'dateTime': data_fim,
            'timeZone': 'America/Sao_Paulo',
        },
    }

    try:
        evento_criado = service.events().insert(calendarId='primary', body=evento).execute()
        print(f"Evento criado: {evento_criado.get('htmlLink')}")
        return evento_criado.get('id')
    except HttpError as error:
        print(f"Erro ao criar o evento: {error}")

def deletar_evento(service, evento_id):
    
    try:
        service.events().delete(calendarId='primary', eventId=evento_id).execute()
        print(f"Evento com ID {evento_id} deletado com sucesso.")
    except HttpError as error:
        print(f"Erro ao deletar o evento: {error}")
