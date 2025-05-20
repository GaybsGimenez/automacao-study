
import requests
import pandas as pd
import streamlit as st



def obter_request(url, params=None):
    """Faz uma requisição GET e retorna a resposta em JSON"""
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        print(f"Erro no request: {e}")
        return None


def frequencia_nome(name):
    """Obtem um dicionário de frequência de nome por década {decada: quantidade}"""
    
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{name}"
    dados_nome = obter_request(url) or []
    #return {dado["periodo"]: dado["frequencia"] for dado in dados_nome[0].get("res", [])}
    dados_dict = {dado["periodo"]: dado["frequencia"] for dado in dados_nome[0].get("res", [])}
    df = pd.DataFrame.from_dict(dados_dict, orient='index')
    return df



def main():
    st.title("Web app API")
    st.header("Dados da API do IBGE")
    in_name = st.text_input("Diginte o nome: \n")
    if not in_name:
        st.stop()
    df = frequencia_nome(in_name)
    col1, col2 = st.columns([0.3, 0.7])
    with col1:
        st.write("Frequência por Década")
        st.dataframe(df)
    with col2:
        st.write("Série Temporal")
        st.line_chart(df)

    #print(frequencia_nome(in_name))
    
if __name__ == "__main__":
    main()