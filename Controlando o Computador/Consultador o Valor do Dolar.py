import pyautogui as posicaoMouse
import pyautogui as tempoEspera

# Threads Sleep
tempoEspera.sleep(2)

# Movendo o mouse até o botão iniciar.
posicaoMouse.moveTo(19, 891)

# Threads Sleep
tempoEspera.sleep(2)

# Clicando na posição presente [ Menu Iniciar ]
posicaoMouse.click()

# Threads Sleep
tempoEspera.sleep(2)

# Digitando o nome do navegador
posicaoMouse.typewrite('edge')

# Threads Sleep
tempoEspera.sleep(2)

# Abrindo o navegador com a tecla Enter.
posicaoMouse.press('enter')

# Threads Sleep
tempoEspera.sleep(2)

# Digitando a palavra Dólar para pesquisar.
posicaoMouse.typewrite('Dolar')

# Threads Sleep
tempoEspera.sleep(2)

# Apertando a tecla [ enter ] para pesquisar a palavra Dólar.
posicaoMouse.press('enter')






