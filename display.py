import time
import os
import ctypes

def estilizacaoConsole(tituloConsole,corConsole):
    ctypes.windll.kernel32.SetConsoleTitleW(tituloConsole)    
    os.system(f"color {corConsole}")
    os.system("mode con: cols=100 lines=3")

def animacaoLogo(logo,creditos):
    for linha in logo:
        print(linha.center(100))
        time.sleep(0.3)

    time.sleep(0.5)
    print("\n" + f"credits: {creditos}".center(100))
    time.sleep(0.5)
    print("\n\n\n")
