import pyautogui
import time



# 1. tamanho da tela
print(pyautogui.size()) 
# Size(width=1920, height=1080)


# 2. pegar a posição atual do cursor
print(pyautogui.position())
# Point(x=948, y=793)

# 3. aplicação para ver a posição do cursor em tempo real
"""
- Digite o comando no terminal  o comando: python (para abri o python no terminal)

>> from pyautogui import mouseInfo
mouseInfo()

"""

# 4. mover o cursor do mouse
pyautogui.moveTo(1785,16) # coordenada do botão de minimizar encontrada com o maouseInfo() no terminal
time.sleep(5) # tempo para chegar até lá
pyautogui.click() # número de clics