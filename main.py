import time
from datetime import datetime
from core import *
from display import *

estilizacaoConsole(tituloConsole,corConsole)
animacaoLogo(logo,creditos)

# for canal, url in slackWebhooks.items():
envia_alerta(mensagem_alerta_inicial(), "padrao")

while True:      
    # Obtendo a hora atual
    hora_atual = datetime.now().strftime('%H:%M:%S')

    #buscando novos chamados
    resposta_chamados_novos = requests.post(buscaChamadoGLPI, headers=cabecalho, json=criterio_chamados_novos)
    quantidade_chamados_novos = json.loads(resposta_chamados_novos.text)["totalcount"]

    if(quantidade_chamados_novos > 0):
        chamados_sanitizados = sanitiza_chamado(resposta_chamados_novos.text)
        chamados_traduzidos = [reformula_chamados(ticket) for ticket in chamados_sanitizados]  
        chamados_separados = separa_chamado(chamados_traduzidos)
        for canal, chamado in chamados_separados.items():    
            if chamado:            
                chamados_indentados = indenta_chamado(chamados_traduzidos)
                envia_alerta(mensagem_padrao_alerta(quantidade_chamados_novos, hora_atual, chamados_indentados), canal) 
    else:
        print(f'[INFO]::Nenhum chamado novo!({hora_atual})')       
   
    temporizador()