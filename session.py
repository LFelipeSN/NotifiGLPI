import requests
from config import *
# cabeçario usado apenas para inicio de sessão
cabecalho_inicioSessao  = {
    "Authorization": f'user_token {sessao_user_token}',
    "App-Token" : sessao_app_token
}

#obtendo cabeçario para consultas na api
try:
    resposta_inicioSessao = requests.get(inicioSessaoGLPI,headers=cabecalho_inicioSessao)
    session_token = json.loads(resposta_inicioSessao.text)["session_token"]

except requests.exceptions.ConnectTimeout:
    input("[ERRO]::Tempo de conexão esgotado (ConnectTimeout)") 
    exit()
except requests.exceptions.ConnectionError:
    input("[ERRO]::Não foi possível conectar ao servidor (ConnectionError)")
    exit()
except Exception as e:
    input(f"[ERRO]::Falha inesperada na requisição -> {e}")
    exit()

cabecalho = {
    "Content-Type": "application/json",
    "App-Token" : sessao_app_token,
    "Session-Token": session_token
}
del cabecalho_inicioSessao
del session_token