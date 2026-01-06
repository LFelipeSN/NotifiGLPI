# NotifiGLPI
NotifiGLPI é um sistema de alertas que monitora novos chamados no GLPI e envia notificações pelo Slack.

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=CONCLUÍDO&color=GREEN&style=for-the-badge)


## Indice
- [Tecnologias Utilizadas](#tecnologias-utilizadas)

- [Execução](#Execução)

- [Autores](#autores)

- [Créditos](#Créditos)

## Tecnologias Utilizadas
- API do GLPI
- API do Slack

## Demonstração


# Execução
É necessário criar um arquivo .json com as informações correspondentes (verificar modelo.json). Após isso, execute o main.py

## Criando executável com pyinstaller
```bash
ps> pyinstaller --onefile --console main.py
ps> move .\dist\main.exe .
```

## Removendo pastas e arquivos desnecessárias
```bash
ps> Remove-Item -Recurse -Force build; Remove-Item -Recurse -Force dist; Remove-Item -Force main.spec
```

## Autores
<div align="left">
  <a href="https://github.com/LFelipeSN" target="_blank">
    <img src="https://github.com/LFelipeSN.png" width="64" height="64" alt="LFelipeSN" style="border-radius:50%;margin-top:8px;" />
  </a>
</div>

## Créditos
- [GLPI Project](https://glpi-project.org/)
- [Slack](https://api.slack.com/)
