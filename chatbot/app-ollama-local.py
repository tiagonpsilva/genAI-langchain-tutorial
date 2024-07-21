from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import  streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

## Langsmith tracking
os.environ['LANGCHAIN_TRACING_V2']="true"
os.environ['LANGCHAIN_API_KEY'] =os.getenv('LANGCHAIN_API_KEY')

#Prompt Template
prompt=ChatPromptTemplate.from_messages([
    ("system","Você é um asistente virtual que pode responder perguntas sobre qualquer coisa. Qual é a sua pergunta?"),
    ("user","Pergunta:{input}")
])

## Streamlit framework
st.title('ChatBot Ollama - LLama3')
input_text=st.text_input("Pode perguntar!")

# Ollama LLM LLama2
llm=Ollama(model="llama3")
output_parser=StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"input": input_text}))