import pyautogui
import time



#pyautogui.write("Olá mundo!")

# abrir windows pesquisa, escrever calculadora e abrir com enter
pyautogui.press("winleft")
time.sleep(1)
pyautogui.write("calculadora", interval=0.15)
pyautogui.press("enter")


#mover curso do mouse para minimizar janela
pyautogui.moveTo(1780, 16, duration=0.7)
time.sleep(1)
pyautogui.click()


# fechar janela
# with pyautogui.hold("alt"):
#     pyautogui.press(["f4"])
    
    
# organizar 2 janelas em uma mesma tela
pyautogui.keyDown("winleft")
pyautogui.press(["left"])
time.sleep(2)
