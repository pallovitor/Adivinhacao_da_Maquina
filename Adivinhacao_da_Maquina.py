import tkinter as tk

def jogo():
    def on_key_press(event):
        nonlocal resposta_real, texto_exibido

        # Ignorar teclas que não são caracteres
        if len(event.char) == 0:
            return "break"

        if event.keysym == "Return":  # Finaliza ao pressionar Enter
            mostrar_popup(f"{resposta_real.strip()}!")
            entrada_entry.config(state="disabled")  # Bloqueia a entrada após finalizar
            return "break"
        elif event.keysym == "BackSpace":  # Apaga o último caractere
            if len(resposta_real) > 0:
                resposta_real = resposta_real[:-1]
                texto_exibido = texto_exibido[:-1]
                entrada_var.set(texto_exibido)  # Atualiza o campo de entrada
                entrada_entry.icursor(len(texto_exibido))  # Ajusta o cursor
            return "break"
        elif len(resposta_real) < 14:  # Limita o texto a 14 caracteres
            resposta_real += event.char.upper()  # Adiciona o caractere real em maiúsculo
            falso_char = texto_falso[(len(resposta_real) - 1) % len(texto_falso)]
            texto_exibido += falso_char.upper()  # Mostra um caractere falso
            entrada_var.set(texto_exibido)  # Atualiza o campo de entrada
            entrada_entry.icursor(len(texto_exibido))  # Ajusta o cursor
            return "break"

    def mostrar_popup(mensagem):
        # Cria uma janela popup para mostrar o resultado
        popup = tk.Toplevel(janela)
        popup.title("Resultado")
        popup.geometry("300x150")
        popup.resizable(False, False)

        # Exibe a mensagem no popup
        mensagem_label = tk.Label(popup, text=mensagem, font=("Arial", 20), wraplength=280, fg="green")
        mensagem_label.pack(pady=20)

        # Botão para fechar o popup
        fechar_button = tk.Button(popup, text="Fechar", command=popup.destroy, font=("Arial", 12))
        fechar_button.pack(pady=10)

    # Configurações iniciais
    texto_falso = "MEU COMPUTADOR"  # Texto que será exibido no lugar do real
    resposta_real = ""  # Armazena o texto real digitado
    texto_exibido = ""  # Armazena o texto falso exibido

    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Jogo de Adivinhação da Máquina")
    janela.geometry("500x300")

    # Título do jogo
    titulo_label = tk.Label(janela, text="Bem-vindo ao jogo de adivinhação da máquina!", font=("Arial", 14))
    titulo_label.pack(pady=10)

    # Instruções para o jogador
    instrucoes_label = tk.Label(janela, text="Pense em uma palavra ou frase e digite abaixo:", font=("Arial", 12))
    instrucoes_label.pack(pady=5)

    # Campo de entrada de texto
    entrada_var = tk.StringVar()
    entrada_entry = tk.Entry(janela, textvariable=entrada_var, font=("Arial", 14), justify="center", state="normal")
    entrada_entry.pack(pady=10)
    entrada_entry.bind("<Key>", on_key_press)  # Captura os eventos de teclado

    # Botão para sair do jogo
    sair_button = tk.Button(janela, text="Sair", command=janela.destroy, font=("Arial", 12))
    sair_button.pack(pady=10)

    # Coloca o foco no campo de entrada
    entrada_entry.focus()

    # Inicia o loop da interface gráfica
    janela.mainloop()

# Executa o jogo
jogo()