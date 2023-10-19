# PROGRAMA PARA AUTOMAÇÃO DE TAREFAS
# Visando preservar as informações da empresa, utilizarei um site fictício.

# Passo 1: Entrar no sistema ou site a ser utilizado na automação.
# Instalação das bibliotecas

import pyautogui
import time

pyautogui.PAUSE = 0.3

# Automatização para abertura do navegador, neste caso, "Microsoft Edge"
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

# Entrar no link do sistema a ser utilizado.
link = "https://xyz.com.br/login"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

# Passo 2: Fazer o login - verificar no arquivo auxiliar como localizar o ponto do mouse que deverá ser considerado.
pyautogui.click(x=471, y=351)
pyautogui.write("jjackson.f@yahoo.com")

pyautogui.press("tab") 
pyautogui.write("sua senha aqui")
pyautogui.press("tab") 
pyautogui.press("enter")

time.sleep(0.3)

# Passo 3: Importar a base de dados.
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    # Passo 4: Cadastrar um produto.
    pyautogui.click(x=403, y=243)

    # Preencher os campos
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

# Condicional para não colocar nada quando obs for "nan".
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    # apartar o botão ENVIAR
    pyautogui.press("tab")
    pyautogui.press("enter")

    #para rolar a página
    pyautogui.scroll(99999) #colocar um número grande para que ele suba até o topo da página

# Passo 5: Repetir o cadastro para todos os produtos.

