import os
import globals

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pauseScreen():
    input("\nPressione <enter> para continuar")
