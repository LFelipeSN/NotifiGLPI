import json
with open("config.json", "r", encoding="utf-8") as f:
    configuracoes = json.load(f)

criterio_chamados_novos = configuracoes["criterios"]["criterio_chamados_novos"]
criterio_chamados_atribuidos = configuracoes["criterios"]["criterio_chamados_atribuidos"]
traducoes_chaves_chamados = configuracoes["traducoes"]["traducoes_chaves_chamados"]
traducoes_localizacoes_para_siglas = configuracoes["traducoes"]["traducoes_localizacoes_para_siglas"]
sessao_app_token = configuracoes["sessao"]["sessao_app_token"]
sessao_user_token = configuracoes["sessao"]["sessao_user_token"]
inicioSessaoGLPI = configuracoes["glpiURL"]+configuracoes["rotasGLPI"]["inicioSessao"]
buscaChamadoGLPI = configuracoes["glpiURL"]+configuracoes["rotasGLPI"]["buscaChamado"]
slackWebhooks = configuracoes["slackWebhooks"]
classificacao_chamados = configuracoes["classificacao_chamados"]
logo = [
    "##    ##                                          ######   ##       ########  ####",
    "###   ##  #######   ######  ####  #######  ####  ##    ##  ##       ##     ##  ## ",
    "####  ## ##     ##    ##     ##   ##        ##   ##        ##       ##     ##  ## ",
    "## ## ## ##     ##    ##     ##   #######   ##   ##   #### ##       ########   ## ",
    "##  #### ##     ##    ##     ##   ##        ##   ##    ##  ##       ##         ## ",
    "##   ### ##     ##    ##     ##   ##        ##   ##    ##  ##       ##         ## ",
    "##    ##  #######     ##    ####  ##       ####   ######   ######## ##        ####"
]
creditos = "LFelipeSN"
tituloConsole ="NotifiGLPI"
corConsole = "0E"
