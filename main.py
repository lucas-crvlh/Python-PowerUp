import pyautogui
import time

pyautogui.PAUSE = 1.5
# Passo 1: Entrar no link do sistema - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# abrir o Chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "shift", "n")

# acessar o site do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Passo 2: Fazer login
# preencher email
pyautogui.click(x=951, y=502)
pyautogui.write("lucas@email.com")

# preencher senha
pyautogui.press("tab")
pyautogui.write("senha")

# clicar em login
pyautogui.press("tab")
pyautogui.press("enter")

# Passo 3: Importar a base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)
pyautogui.click(x=1190, y=450)
time.sleep(2)

# Passo 4: Cadastrar 1 produto
for linha in tabela.index:
    pyautogui.click(x=833, y=358)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)

    pyautogui.press("tab")
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = str(tabela.loc[linha, "tipo"])   
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.ress("enter") # bug enter não funciona no botão "Enviar"
    pyautogui.scroll(10000)

# Passo 5: Repetir para todos os produtos
