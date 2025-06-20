import pyautogui
import time


#miniza tela e printa tela de baixo
# pyautogui.moveTo(1785,16, duration=0.7) 
# time.sleep(5) 
# pyautogui.click() 
# time.sleep(1)

# # gerar uma imagem
# pyautogui.screenshot("doc.png")
# pyautogui.alert(text="Imagem salva com sucesso!", title="Captura de imagem", button="OK")


# gerar varias imagens de 3s em 3s
while True:
    pyautogui.screenshot(f"image_{time.time()}.png")
    time.sleep(3)