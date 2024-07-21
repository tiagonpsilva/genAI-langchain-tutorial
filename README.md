# LangChain Tutorial

Exemplos de implementação do LangChain

## Referência

https://www.youtube.com/watch?v=swCPic00c30

## Tech Stack

- Python 3.8
- OpenAI GPT-3
- Streamlit
- FastAPI
- Uvicorn
- Requests

## :file_folder: Estrutura do Projeto

| Arquivo/Diretório | Descrição |
| --- | --- |
| `.env` | Arquivo para definir variáveis de ambiente |
| `README.md` | Documentação inicial do projeto |
| `api/` | Diretório contendo os arquivos `app.py` e `client.py` para a API |
| `chatbot/` | Diretório contendo os arquivos `app-chatgpt.py` e `app-ollama-local.py` para o chatbot |
| `requirements.txt` | Arquivo contendo as dependências do projeto |
| `venv/` | Diretório do ambiente virtual Python |

## Variáveis de Ambiente

- OPENAI_API_KEY: Chave da API OpenAI
- LANGCHAIN_TRACING_V2: Habilita o rastreamento do LangChain
- LANGCHAIN_API_KEY: Chave da API LangChain

## :wrench: Instalação para Uso Local

O projeto requer as seguintes bibliotecas:

- openai
- os
- dotenv
- fastapi
- uvicorn
- streamlit
- requests


Para instalar as dependências, execute o seguinte comando:

```sh
pip install -r requirements.txt
```
### ChatBot Front + LLM

Para executar o chatbot conectado no LLM GPT-3 Turbo:
```sh
streamlit run chatbot/app-chatgpt.py
```

Para executar o chatbot conectado no LLM LLama3, pelo Ollama (de forma local):
```sh
streamlit run chatbot/app-chatgpt.py
```
Neste caso, é necessário instalar o Ollama e baixar o modelo LLama3


### ChatBot Front + API Server + LLM

Para subir o servidor que expõe a API
```sh
python3 api/app.py
```
Após subir o servidor, a documentação da API (swagger) pode ser acessada pelo navegador
http://localhost:8000/docs#/

Para executar a aplicação client que consome a API:
```sh
streamlit run api/client.py
```
Neste caso, é necessário instalar o Ollama e baixar o modelo LLama3 para usar o segundo input text do client