import requests
import streamlit as st

def get_llm1_response(prompt):
    """
    Esta função envia uma requisição POST para o endpoint /teams/invoke com o prompt fornecido como entrada.
    Ela retorna o campo 'content' da saída da resposta.

    Args:
        prompt (str): O nome do país.

    Returns:
        str: O conteúdo da saída da resposta.
    """
    url = "http://localhost:8000/teams/invoke"
    data = {"input": {'country': prompt}}

    response = requests.post(url,json=data)
    return response.json()['output']['content']

def get_llm2_response(prompt):
    """
    Esta função envia uma requisição POST para o endpoint /details/invoke com o prompt fornecido como entrada.
    Ela retorna o campo 'output' da resposta.

    Args:
        prompt (str): O nome do país.

    Returns:
        dict: A saída da resposta.
    """
    url = "http://localhost:8000/details/invoke"
    data = {"input": {'country': prompt}}

    response = requests.post(url,json=data)
    return response.json()['output']

## Aplicativo Streamlit
st.title("Cliente Streamlit Langchain - Futebol no Mundo")
input_text1 = st.text_input("Digite o nome do país para saber a lista de times:")
input_text2 = st.text_input("Digite o nome do país a populariadade do futebol:")

if input_text1:
    st.write(get_llm1_response(input_text1))

if input_text2:
    st.write(get_llm2_response(input_text2))