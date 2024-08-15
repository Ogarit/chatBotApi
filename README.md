# ChatBot API

Este projeto é uma API de chatbot construída usando Django. Ele fornece uma estrutura básica para o desenvolvimento de APIs que podem ser integradas a sistemas de chat.

## Estrutura do Projeto

- **chat_bot/**
  - Contém a aplicação principal do Django, incluindo os arquivos de configuração e a API.
  
  - **api/**
    - Contém a lógica da API, incluindo models, views, urls, e a configuração do admin.

  - **chat_bot/**
    - Contém os arquivos de configuração do projeto Django, como `settings.py`, `urls.py`, e os módulos `wsgi.py` e `asgi.py`.

## Funcionalidades

- **API de Chatbot**: Um ponto de partida para criar e gerenciar um chatbot usando Django.
- **Administração**: O módulo `admin.py` permite que você gerencie modelos da API através da interface de administração do Django.
- **Testes**: O módulo `tests.py` contém testes básicos para garantir a funcionalidade da API.

## Requisitos

- Python 3.x
- Django 3.x

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/chatBotApi.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd chatBotApi
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```
5. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

## Como Usar

- Acesse a API através do endpoint `/api/`.
- Use as configurações no arquivo `settings.py` para ajustar o projeto às suas necessidades.

## Contribuição

Se você quiser contribuir para este projeto, faça um fork do repositório e envie um pull request com suas mudanças.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
