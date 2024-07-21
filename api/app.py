from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os  
from langchain_community.llms import Ollama

from dotenv import load_dotenv
load_dotenv()

# Carrega a chave da API OpenAI do arquivo .env
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="Langchain API Server - Futebol no Mundo",
    version="1.0",
    description="Detalhes sobre como é o futebol em diferentes países",
)

# Adiciona rotas para o modelo de chat OpenAI
add_routes(
    app,
    ChatOpenAI(),
    path="/openai",
)

# Cria instâncias dos modelos de linguagem
llm1=ChatOpenAI()
llm2=Ollama(model="llama3")

# Cria prompts para os modelos de linguagem
prompt1 = ChatPromptTemplate.from_template("Liste os principais times de futebol localizados no país: {country}?")
prompt2 = ChatPromptTemplate.from_template("Conte-me sobre a popularidade do futebol no país: {country}?")

# Adiciona rotas para os prompts e modelos de linguagem
add_routes(
    app,
    prompt1 | llm1,
    path="/teams",
)

add_routes(
    app,
    prompt2 | llm2,
    path="/details",
)

# Inicia o servidor FastAPI
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)