import pyautogui as posicaoAbreArquivos


# Pressionar duas teclas ao mesmo tempo
# Windows + R ( para abrir o menu Executar )
posicaoAbreArquivos.hotkey('win', 'r')

# Threads sleep
posicaoAbreArquivos.sleep(2)

# Será digitado ( notepad ) na caixa de texto do menu executar
posicaoAbreArquivos.typewrite('notepad')

# Threads sleep
posicaoAbreArquivos.sleep(2)

# Será pressionado o ( Enter ), e por tanto abrirá o Bloco de Notas
posicaoAbreArquivos.press('enter')

# Threads sleep
posicaoAbreArquivos.sleep(2)

# Digitando o que for passado nos parâmetros dentro do bloco de Notas.
posicaoAbreArquivos.typewrite('Abri o Bloco de Notas com o Python.')

# Threads sleep
posicaoAbreArquivos.sleep(2)

# Permite pegar a janela que está ativa
fecharBlocoDeNotas = posicaoAbreArquivos.getActiveWindow()

# Threads sleep
posicaoAbreArquivos.sleep(2)

# Aciona a opção para fechar a janela ativa
fecharBlocoDeNotas.close()

# Threads sleep
posicaoAbreArquivos.sleep(2)

# Pressionado a tecla tab, para pular de Salvar para Não Salvar
posicaoAbreArquivos.press('tab')

# Threads sleep
posicaoAbreArquivos.sleep(2)

# Fechando o documento sem Salvar
posicaoAbreArquivos.press('enter')





