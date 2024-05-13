# pip install flet
# passos para usar o flet
# 1 - importar o flet
# 2 - criar a função principal
# 3 - rodar o aplicativo

#-----------------------------------------------------------------------------------------------------------------------

# 1 - importar o flet
import flet as ft

# 2 - criar a função principal
def main(pagina):
  # criar as funcionalidades
  
  # criar o elemento de texto
  titulo = ft.Text("Hashzap")
  
  titulo_janela = ft.Text("Olá")
  campo_nome_usuario = ft.TextField(label="Escreva seu nome")
  
  chat = ft.Column()
  campo_mensagem = ft.TextField(label="Digite sua mensagem")
  
  def enviar_mensagem(evento):
    print("")
        
  botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    
  linha_mensagem = ft.Row([campo_mensagem,botao_enviar_mensagem])
  def entrar_chat(evento):
    pagina.remove(titulo)
    pagina.remove(botao_iniciar)
    janela.open = False
    pagina.add(chat)
    pagina.add(linha_mensagem)
    pagina.update()

  botao_entrar = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)
  janela = ft.AlertDialog(title=titulo_janela, content=campo_nome_usuario, actions=[botao_entrar])
  
  def iniciar_chat(evento):
    pagina.dialog = janela
    janela.open = True
    pagina.update()
    
  botao_iniciar = ft.ElevatedButton("iniciar Chat", on_click=iniciar_chat)
  # chat = ft.Column()
  # nome_usuario = ft.TextField(label="Escreva seu nome")
  
  # adiciona o elemento na pagina
  pagina.add(titulo)
  pagina.add(botao_iniciar)

# 3 - rodar o aplicativo
ft.app(target=main, view=ft.WEB_BROWSER)


#def enviar_mensagem_tunel(mensagem):
#   tipo = mensagem["tipo"]
#   if tipo == "mensagem":
#     texto_mensagem = mensagem["texto"]
#     usuario_mensagem = mensagem["usuario"]
#     # adicionar a mensagem no chat
#     chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))
#   else:
#     usuario_mensagem = mensagem["usuario"]
#     chat.controls.append(ft.Text(f"{usuario_mensagem} entrou no chat",
#                                   size=12, italic=True, color=ft.colors.ORANGE_500))
#   pagina.update()

# pagina.pubsub.subscribe(enviar_mensagem_tunel)

# def enviar_mensagem(evento):
#   pagina.pubsub.send_all({"texto": campo_mensagem.value, "usuario": nome_usuario.value,
#                           "tipo": "mensagem"})
#   # limpar o campo de mensagem
#   campo_mensagem.value = ""
#   pagina.update()

# campo_mensagem = ft.TextField(label="Digite uma mensagem", on_submit=enviar_mensagem)
# botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

# def entrar_popup(evento):
#   pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
#   # adicionar o chat
#   pagina.add(chat)
#   # fechar o popup
#   popup.open = False
#   # remover o botao iniciar chat
#   pagina.remove(botao_iniciar)
#   pagina.remove(texto)
#   # criar o campo de mensagem do usuario
#   # criar o botao de enviar mensagem do usuario
#   pagina.add(ft.Row(
#       [campo_mensagem, botao_enviar_mensagem]
#   ))
#   pagina.update()

# popup = ft.AlertDialog(
#     open=False,
#     modal=True,
#     title=ft.Text("Bem vindo ao Hashzap"),
#     content=nome_usuario,
#     actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)],
#     )

# def entrar_chat(evento):
#   pagina.dialog = popup
#   popup.open = True
#   pagina.update()

# botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=entrar_chat)

# pagina.add(texto)
# pagina.add(botao_iniciar)



# deploy
