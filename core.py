import requests
from tqdm import trange
from datetime import datetime
import html
import re
import time
from config import *
from session import *

#mensagem enviada para o canal quando um alerta é encontrado
def mensagem_padrao_alerta(quantidade_chamados_novos, hora_atual, chamados_indentados):
    mensagem = f"""
======== 📢 ALERTA ========= \n
🕖Horário Atual: {hora_atual} \n
🚨Chamados Novos: {quantidade_chamados_novos}\n
⚠️Obs: você deve atribuir o chamado para que ele pare de notificar⚠️
--------------------------------------------- \n 
{chamados_indentados} \n 
---------------------------------------------"""
    
    return mensagem
#mensagem inicial de resumo  
def mensagem_alerta_inicial():#canal,url
    # classificacao_chamados[canal]
    quantidade_chamados_novos = json.loads(busca_chamados_novos().text)["totalcount"]#canal
    quantidade_chamados_atribuidos = json.loads(busca_chamados_atribuidos().text)["totalcount"]#canal

    mensagem_inicial = f"""
======== 📊 RESUMO ATUAL ========\n 
🚨Chamados Novos: {quantidade_chamados_novos}\n 
📝Chamados Atribuídos: {quantidade_chamados_atribuidos}\n 
⚠️Não se esqueça de conferi-los⚠️ \n 
-----------------------------------------------"""
    
    return mensagem_inicial

#envia o alerta utilizando a api do whatsapp
def envia_alerta(mensagem, canal):
    payload = {"text": mensagem}
    print(f'[INFO]::{mensagem}')
    resposta_alerta_numero = requests.post(slackWebhooks[canal], json=payload)
    print(f'\n [INFO]::Alerta enviado para o canal "{canal}" :: {resposta_alerta_numero.text} \n')

def separa_chamado(chamado):
    chamados_separados = {"padrao": chamado}
    for classificacao, criterio in classificacao_chamados.items(): 

        chamados_encontrados = []
        for chamado in chamados_separados['padrao']: 
            if chamado['🗳️Categoria'].startswith(criterio):
                chamados_encontrados.append(chamado) 

        chamados_separados[classificacao] = chamados_encontrados
    return chamados_separados

def indenta_chamado(chamado):
    chamados_indentado = json.dumps(chamado,indent=0, ensure_ascii=False)
    chamados_indentado = re.sub(r'<[^>]+>|\[|\]|\{|\}|\"|\,\n|\\n', lambda m: '\n' if m.group() in ['<p>', '<br>',',\n'] else '', chamados_indentado)
    return chamados_indentado

#troca os nomes das chaves de acordo com as traducoes e retira chaves desnesessarias
def reformula_chamados(chamado):
    chamado_traduzido = {}
    for chave, valor in chamado.items():
        nova_chave = traducoes_chaves_chamados.get(chave, chave)

        if chave == 'Ticket.status':
            continue
        elif chave == 'Ticket.Location.completename':
            valor = traducoes_localizacoes_para_siglas.get(valor, valor)   
        elif chave == 'Ticket.date':
            valor = datetime.strptime(valor, "%Y-%m-%d %H:%M:%S").strftime("%d/%m/%Y")

        chamado_traduzido[nova_chave] = valor
    return chamado_traduzido

#remove caracteres especias e trasnforma a mensagem para um obj phyton
def sanitiza_chamado(chamado):
    chamados_sanitizados = html.unescape(chamado)
    chamados_sanitizados = json.loads(chamados_sanitizados)["data"]
    return chamados_sanitizados

def busca_chamados_novos():
    return requests.post(buscaChamadoGLPI, headers=cabecalho, json=criterio_chamados_novos)

def busca_chamados_atribuidos():
    return requests.post(buscaChamadoGLPI, headers=cabecalho, json=criterio_chamados_atribuidos)

def temporizador(tempo=300):
    for _ in trange(tempo, desc="[INFO]::Aguardando próxima verificação"):
        time.sleep(1)