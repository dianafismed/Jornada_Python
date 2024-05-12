# Passo a passo

# pip install pyautogui
# pandas numpy openpyxl

# bibliotecas
import pyautogui as pag
import time
import pandas as pd

pag.PAUSE = 0.75 # quer dizer que a cada comando efetuado o sistema vai esperar 0,75 segundos até o próximo
# pag.click -> clicar com o mouse
# pag.write -> escrever um texto
# pag.press -> pressionar uma tecla do teclado
# pag.hotkey -> pressiona um conjunto de teclas

# 1. Abrir o sistema
# abrir o navegador
pag.press("win")
pag.write("firefox")
pag.press("enter")
# entrar no site (https://dlp.hashtagtreinamentos.com/python/intensivao/login)
pag.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pag.press("enter")
time.sleep(3) # dá uma pausa de 3 segundos somente neste ponto

# 2. Fazer login
pag.click(x=-1243, y=89)
pag.write("dianafismed@yahoo.com.br")
pag.press("tab")
pag.write("senha")
pag.press("tab")
pag.press("enter")
time.sleep(3)

# 3. Abrir/ importar a base de dados de produtos para cadastrar
tabela = pd.read_csv("produtos.csv")

# 4. Cadastrar os produtos
# codigo,marca,tipo,categoria,preco_unitario,custo,obs
for linha in tabela.index:  # para cada linha da minha tabela
  pag.click(x=-1252, y=-32)
  pag.write(tabela.loc[linha,"codigo"])
  pag.press("tab")
  pag.write(tabela.loc[linha,"marca"])
  pag.press("tab")
  pag.write(tabela.loc[linha,"tipo"])2
  pag.press("tab")
  pag.write(str(tabela.loc[linha,"categoria"]))
  pag.press("tab")
  pag.write(str(tabela.loc[linha,"preco_unitario"]))
  pag.press("tab")
  pag.write(str(tabela.loc[linha,"custo"]))
  pag.press("tab")
  obs = str(tabela.loc[linha,"obs"])
  if (obs != "nan"):
    pag.write(obs)
  pag.press("tab")
  pag.press("enter")
  pag.scroll(5000) # pag.press("home")



