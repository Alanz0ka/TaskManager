import os
import pickle
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar']

def iniciar_google_calendar():
    """Inicializa o serviço do Google Calendar usando credenciais armazenadas ou solicitando novas."""
    credenciais = None

    # Verifica se o arquivo de token existe e carrega as credenciais
    if os.path.exists("token.pickle"):
        with open('token.pickle', 'rb') as token:
            credenciais = pickle.load(token)

    # Se as credenciais não estiverem disponíveis ou forem inválidas
    if not credenciais or not credenciais.valid:
        if credenciais and credenciais.expired and credenciais.refresh_token:
            try:
                credenciais.refresh(Request())
            except Exception as e:
                print(f"Erro ao atualizar as credenciais: {e}")
                credenciais = None
        else:
            # Solicita novas credenciais
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            credenciais = flow.run_local_server(port=0)

        # Salva as novas credenciais em um arquivo
        with open('token.pickle', 'wb') as token:
            pickle.dump(credenciais, token)

    # Inicializa o serviço do Google Calendar
    servico = build('calendar', 'v3', credentials=credenciais)
    return servico

def criar_evento(service, resumo, descricao, data_inicio, data_fim):
    """Cria um evento no Google Calendar."""
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
    except HttpError as error:
        print(f"Erro ao criar o evento: {error}")
