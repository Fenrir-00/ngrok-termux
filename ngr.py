import sys
from sys import *
import os 
from os import *
import time
from io import *
class color:
    morado = '\033[95m'
    blanco = '\033[97m'
    cyan = '\033[96m'
    azul  = '\033[94m'
    verde = '\033[92m'
    amarillo = '\033[93m'
    rojo = '\033[91m'
    fin = '\033[0m'

os.system("chmod +x ngrok")
def banner():
 os.system("clear")
 print(f"""{color.cyan}
███████╗███████╗███╗  ██╗██████╗ ██╗██████╗
██╔════ ██╔════╝████╗ ██║██╔══██╗██║██╔══██╗
█████╗  █████╗  ██╔██╗██║██████╔╝██║██████╔╝
██╔══   ██╔══╝  ██║╚████║██╔══██╗██║██╔══██╗
██║     ███████╗██║ ╚███║██║  ██║██║██║  ██║
╚═╝     ╚══════╝╚═╝  ╚══╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝""")
 print(f"{color.fin}")

#barra de carga
def carga():
    print(f"{color.verde}")
    print("""Loading…
    █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…10%
    ███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…30%
    █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…50%
    ██████████▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…70%
    █████████████▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…100%
    ███████████████████""")
    time.sleep(1)
    os.system("clear")
    banner()
#menu principal

def menu():
    os.system("clear")
    banner()
    carga()
    print(f"{color.verde}    .....NGROK.....")
    print("")
    print(f"{color.verde}[1]INCIAR NGROK TCP 4444")
    print(f"{color.verde}[2]ELEGIR MANUAL TCP ")
    print("[3]INCIAR NGROK HTTP 8080")
    print(f"{color.verde}[4]ELEGIR MANUAL HTTP ")
    print(f"{color.amarillo}[5]PONER AUTOKEN")
    print(f"{color.rojo}[6]SALIR{color.fin}")
    eleccion =input(f"{color.cyan}ELIJE UN NUMERO >> ")
    while len(eleccion) >= 2:
     print(len(eleccion))
     os.system("clear")
     banner()
     print(f"{color.verde}    .....NGROK.....")
     print("")
     print(f"{color.verde}[1]INCIAR NGROK TCP 4444")
     print(f"{color.verde}[2]ELEGIR MANUAL TCP ")
     print("[3]INCIAR NGROK HTTP 8080")
     print(f"{color.verde}[4]ELEGIR MANUAL HTTP ")
     print(f"{color.amarillo}[5]PONER AUTOKEN")
     print(f"{color.rojo}[6]SALIR{color.fin}")
     eleccion =input(f"{color.cyan}ELIJE UN NUMERO >> ")
    if eleccion == "1" :
        banner()
        os.system("./ngrok tcp 4444")

    elif eleccion == "2" :
        banner()
        var=input(f"{color.cyan}INTROCUDE TU TCP >>> {color.fin}")
        while len(var) != 4:
         print(f"¨{color.verde}INTROCUDE UN TCP CORRECTO DE 4 DIGITOS")
         var=input(f"{color.cyan}INTROCUDE TU TCP >>> {color.fin}")
        os.system(f"./ngrok tcp {var}"  )

    elif eleccion == "3" :
        banner()
        os.system("./ngrok http 8080")
    elif eleccion == "4" :
        banner()
        var=input(f"{color.cyan}INTROCUDE TU HTTP >>> {color.fin}")
        while len(var) != 4:
         print(f"¨{color.verde}INTROCUDE UN HTTP CORRECTO DE 4 DIGITOS")
         var=input(f"{color.cyan}INTROCUDE TU HTTP >>> {color.fin}")
        os.system(f"./ngrok http {var}"  )   
    elif eleccion == "5" :
     banner()
     print(f"{color.amarillo}INTRODUCE TU AUTOKEN REGISTRANDOTE EN")
     print("        www.ngrok.com")
     print("EJEMPLO: ngrok authtoken 24tEStwKDPJhPb7CRY5PMdikK4F....")
     print("")
     var=input(f"{color.cyan}introduce tu token >>> ")
     os.system(f"./{var}"  )
    
    elif eleccion == "6" :
     banner()
     salir()
    else:
        incorrecto()
# salir


def salir():
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…
    █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…10%
    ███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…30%
    █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…50%
    ██████████▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…70%
    █████████████▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…100%
    ███████████████████""")
    time.sleep(1)
    os.system("clear")
    print(f"{color.fin}")
    sys.exit()
def incorrecto():
    os.system("clear")
    print(f"""{color.rojo}
░█████╗░██████╗░░█████╗░██╗░█████╗░███╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗░██║
██║░░██║██████╔╝██║░░╚═╝██║██║░░██║██╔██╗██║
██║░░██║██╔═══╝░██║░░██╗██║██║░░██║██║╚████║
╚█████╔╝██║░░░░░╚█████╔╝██║╚█████╔╝██║░╚███║
░╚════╝░╚═╝░░░░░░╚════╝░╚═╝░╚════╝░╚═╝░░╚══╝


██╗███╗░░██╗░█████╗░░█████╗░██████╗░██████╗░
██║████╗░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║██╔██╗██║██║░░╚═╝██║░░██║██████╔╝██████╔╝
██║██║╚████║██║░░██╗██║░░██║██╔══██╗██╔══██╗
██║██║░╚███║╚█████╔╝╚█████╔╝██║░░██║██║░░██║
╚═╝╚═╝░░╚══╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝

███████╗░█████╗░████████╗░█████╗░
██╔════╝██╔══██╗╚══██╔══╝██╔══██╗
█████╗░░██║░░╚═╝░░░██║░░░███████║
██╔══╝░░██║░░██╗░░░██║░░░██╔══██║
███████╗╚█████╔╝░░░██║░░░██║░░██║
╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝{color.fin}""")
    time.sleep(4)
    menu()
menu()
os.system("clear")
banner()
print(f"{color.rojo}        ...... ADIOS .......{color.fin}")
