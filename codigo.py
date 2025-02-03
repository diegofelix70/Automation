import pandas
import pandas as pd
import openpyxl
import pyautogui
pyautogui.PAUSE = 0.5 # Not works in the middle of code


from time import sleep

# Just put inside what you want that python click
pyautogui.press("win")

pyautogui.write("Google")

pyautogui.press("enter")

#sleep(1) # This fuction is not from class, but my self

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

pyautogui.press("enter")

sleep(1) # recommended for slow intenet

pyautogui.click(x=779, y=368)

pyautogui.write("HelloWord@email.com ")

pyautogui.press("tab")

pyautogui.write("SenhaSenhaSenhaSenha")

pyautogui.press("tab")

pyautogui.press("enter")

try:
    tabela = pd.read_csv(r"C:\Users\diego\Documents\@Programação\Curso Hashtag Prog\automação\produtos.csv")
    print(tabela)
except Exception as e:
    print(f"Erro ao ler o CSV: {e}")

sleep(1)

# codigo,marca,tipo,categoria,preco_unitario,custo,obs

for indice, linha in tabela.iterrows():
    codigo = linha['codigo']
    marca = linha['marca']
    tipo = linha['tipo']
    categoria = linha['categoria']
    preco_unitario = linha['preco_unitario']
    custo = linha['custo']
    obs = linha['obs']

    pyautogui.click(x=674, y=271)

    #codigo
    
    pyautogui.write(codigo)
    pyautogui.press("tab")

    pyautogui.write(marca)
    pyautogui.press("tab")

    pyautogui.write(tipo)
    pyautogui.press("tab")

    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    pyautogui.write(str(custo))
    pyautogui.press("tab")


    if pd.isna(obs) or obs.strip() == '':
        pyautogui.press("tab")
    else:
        pyautogui.write(obs)
        pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(1000)
