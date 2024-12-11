# ChatBot API

Este projeto é uma API de chatbot desenvolvida com Django, que fornece uma base sólida para integrar sistemas de chat. Ele oferece funcionalidades essenciais para a criação e gestão de chatbots, além de possibilitar a customização e a integração com outras aplicações.

## Estrutura do Projeto

- **chat_bot/**  
  Contém a aplicação principal do Django, com os arquivos de configuração e a API.

  - **api/**  
    Contém a lógica da API, incluindo models, views, URLs e configuração do admin.

- **chat_bot/**  
  Contém arquivos de configuração do projeto Django, como `settings.py`, `urls.py`, além dos módulos `wsgi.py` e `asgi.py`.

## Funcionalidades

- **API de Chatbot**: Um ponto de partida básico para criar e gerenciar um chatbot.  
- **Administração**: O módulo `admin.py` permite gerenciar modelos da API através da interface de administração do Django.
- **Testes**: O módulo `tests.py` contém testes básicos para garantir a funcionalidade da API.
- **Autenticação (Opcional)**: Sistema de autenticação pode ser adicionado facilmente via Django Rest Framework ou outra biblioteca, dependendo das necessidades.
- **Documentação da API**: A API pode ser documentada automaticamente usando ferramentas como Swagger ou DRF-YASG.

## Requisitos

- Python 3.x
- Django 3.x ou superior
- (Opcional) Django Rest Framework, se desejar criar endpoints mais complexos.

## Instalação

Siga os passos abaixo para configurar e rodar o projeto localmente:

1. Clone o repositório:
   ```bash
   git clone https://github.com/Ogarit/chatBotApi.git
2. Navegue até o diretório do projeto:
   ```bash
   cd chatBotApi
3. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use venv\Scripts\activate
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
5. Execute as migrações do banco de dados:
   ```bash
   python manage.py migrate
6. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
Acesse a API no seu navegador em http://127.0.0.1:8000/api/.

## Como Usar

- A API está disponível no endpoint `/api/`.
- Para personalizar o comportamento do chatbot, edite os modelos e views em `chat_bot/api/`.
- As configurações iniciais podem ser ajustadas em `chat_bot/settings.py`.

## Contribuição

Se você quiser contribuir para este projeto, siga estas etapas:
1. Faça um fork do repositório.
2. Crie uma branch para a sua feature (`git checkout -b feature/nova-feature`).
3. Faça o commit das suas alterações (`git commit -am 'Adicionando nova feature'`).
4. Envie para o repositório remoto (`git push origin feature/nova-feature`).
5. Abra um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
