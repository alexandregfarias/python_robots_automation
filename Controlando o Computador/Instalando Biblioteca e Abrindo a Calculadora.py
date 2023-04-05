import pyautogui as posicaoMouse
import pyautogui as tempoEspera

# Tempo de Espera
tempoEspera.sleep(2)

# Movendo o mouse até o botão iniciar.
posicaoMouse.moveTo(19, 891)

# Tempo de Espera
tempoEspera.sleep(2)

# Clicando na posição.
posicaoMouse.click(19, 891)

tempoEspera.sleep(2)

# Escrevendo
posicaoMouse.typewrite('calculadora')

tempoEspera.sleep(2)

# Clicando na posição X, Y
posicaoMouse.click(x=146, y=345)


