# TaskManager API

## O que é
A TaskManager API é uma aplicação desenvolvida em Django para gerenciar tarefas e eventos. Ela permite criar, listar, atualizar e deletar tarefas, com integração ao Google Calendar para adicionar eventos relacionados às tarefas.

## Para que serve
A API serve para organizar e automatizar a gestão de tarefas, permitindo que cada tarefa criada na aplicação também seja adicionada ao Google Calendar. O usuário pode acessar, editar ou deletar tarefas, o que reflete diretamente no calendário integrado.

## Como preparar para usar
### Pré-requisitos
- Python 3.8 ou superior
- Django 5.x
- Google API Client Library
- Um projeto configurado no Google Cloud com a API do Google Calendar ativada

### Instalação e Configuração
1. Clone o repositório do projeto: `git clone https://github.com/seu-repositorio/taskmanager.git`
2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/Mac
    venv\\Scripts\\activate   # Para Windows
    ```
3. Instale as dependências: 
    ```bash
    pip install -r requirements.txt
    ```
4. Configure as credenciais da API do Google Calendar:
    - Obtenha o arquivo `credentials.json` da sua conta no Google Cloud e coloque-o na raiz do projeto.
5. Execute as migrações do Django:
    ```bash
    python manage.py migrate
    ```
6. Inicie o servidor Django:
    ```bash
    python manage.py runserver
    ```

## Como usar
### Aviso Importante:
- **Certifique-se de adicionar uma `/` no final da URL em todas as requisições**. Caso contrário, você receberá um erro `404`.

### Método GET
- **URL**: `/api/v1/task/`
- **Descrição**: Recupera a lista de todas as tarefas ou filtra por título e datas.
- **Parâmetros opcionais**:
    - `data_inicio`: filtra tarefas a partir de uma data específica.
    - `data_fim`: filtra tarefas até uma data específica.
    - `titulo`: filtra tarefas pelo título.
- **Exemplo**:
    ```bash
    "http://localhost:8000/api/v1/task/?titulo=Compra&data_inicio=2024-09-10"
    ```

### Método POST (Criar uma Tarefa)
- **URL**: `http://localhost:8000/api/v1/task/`
- **Descrição**: Cria uma nova tarefa e adiciona um evento no Google Calendar.
- **Exemplo**:
    ```bash
    {
  "titulo": "Campeonato de Jiu-jitsu",
  "descricao": "Vou amassar geral",
  "data": "2024-09-13",
  "horario": "20:00:00"
    } 
    ```



### Método PUT (Atualizar uma Tarefa)
- **URL**: `http://127.0.0.1:8000/api/v1/task/10/`
- **Descrição**: Atualiza uma tarefa existente.
- **Exemplo**:
    ```bash
    {
        "id": 10,
        "titulo": "Tarefa Atualizada",
        "descricao": "tarefa que faz determinada coisa",
        "data": "2024-09-13",
        "horario": "20:00:00"

    }
    ```

### Método DELETE (Deletar uma Tarefa)
- **URL**: `/api/v1/task/10/`
- **Descrição**: Deleta uma tarefa existente e remove o evento associado no Google Calendar.


## Outros Detalhes Relevantes
- O projeto foi configurado para usar a integração com o Google Calendar, por isso, é necessário um arquivo `credentials.json` válido.
- A autenticação do Google Calendar é feita via OAuth 2.0, e as credenciais são salvas no arquivo `token.pickle` para reutilização.