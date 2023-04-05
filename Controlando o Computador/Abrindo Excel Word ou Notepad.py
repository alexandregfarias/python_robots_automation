import pyautogui as escolha_opcao

opcao = escolha_opcao.confirm('Clique no botão desejado',
          buttons=['Excel', 'Wordpad', 'Notepad'])

if opcao == "Excel":

    # Abrindo o Menu Executar
    escolha_opcao.hotkey('win', 'r')

    # Interrompendo a Thread por 2 segundos
    escolha_opcao.sleep(2)

    # Escrevendo Excel na caixa de texto do menu Executar.
    escolha_opcao.typewrite('Excel')

    # Interrompendo a Thread por 2 segundos
    escolha_opcao.sleep(2)

    # Pressionado a teclar Enter para abrir o Excel
    escolha_opcao.press('Enter')

    # Interrompendo a Thread por 2 segundos
    escolha_opcao.sleep(2)


elif opcao == "Wordpad":

    # Abrindo o Menu Executar
    escolha_opcao.hotkey('win', 'r')

    # Interrompendo a Thread por 2 segundos
    escolha_opcao.sleep(1)

    # Escrevendo Excel na caixa de texto do menu Executar.
    escolha_opcao.typewrite('wordpad')

    # Interrompendo a Thread por 2 segundos
    escolha_opcao.sleep(1)

    # Pressionado a teclar Enter para abrir o Excel
    escolha_opcao.press('Enter')

    # Interrompendo a Thread por 2 segundos
    escolha_opcao.sleep(3)

    fecharWordpad = escolha_opcao.getActiveWindow()

    escolha_opcao.sleep(2)

    fecharWordpad.close()



else:

    # Abrindo o Menu Executar
    escolha_opcao.hotkey('win', 'r')

    # Interrompendo a Thread por 2 segundos
    escolha_opcao.sleep(1)

    # Escrevendo Excel na caixa de texto do menu Executar.
    escolha_opcao.typewrite('notepad')

    # Interrompendo a Thread por 2 segundos
    escolha_opcao.sleep(1)

    # Pressionado a teclar Enter para abrir o Excel
    escolha_opcao.press('Enter')

    # Interrompendo a Thread por 2 segundos
    escolha_opcao.sleep(2)

    fecharWordpad = escolha_opcao.getActiveWindow()

    escolha_opcao.sleep(2)

    fecharWordpad.close()




