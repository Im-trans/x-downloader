import os
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import yt_dlp

def baixar_video_twitter():
    url = url_entry.get()
    pasta_download = pasta_entry.get()

    if not url:
        log_text.insert(tk.END, "Erro: URL não pode estar vazia.\n")
        return

    if not pasta_download:
        log_text.insert(tk.END, "Erro: Selecione uma pasta de download.\n")
        return

    try:
        ydl_opts = {
            'outtmpl': f'{pasta_download}/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',  # Força a saída em MP4
        }

        log_text.insert(tk.END, f"Iniciando download do vídeo...\n")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        log_text.insert(tk.END, f"Download concluído! Vídeo salvo em: {pasta_download}\n")

    except Exception as e:
        log_text.insert(tk.END, f"Erro ao baixar o vídeo: {e}\n")


def selecionar_pasta():
    pasta_selecionada = filedialog.askdirectory()
    pasta_entry.delete(0, tk.END)
    pasta_entry.insert(0, pasta_selecionada)


def fechar_aplicacao():
    root.destroy()


# Configuração da interface gráfica
root = tk.Tk()
root.title("Twitter Video Downloader")

root.resizable(False, False)
root.attributes("-toolwindow", True)

# Configuração dos componentes na interface gráfica
root.geometry("730x300")

# Label e Entry para a URL do vídeo
tk.Label(root, text="Link do Vídeo:").place(x=10, y=10)
url_entry = tk.Entry(root, width=70)
url_entry.place(x=120, y=10)

# Label e Entry para a pasta de destino
tk.Label(root, text="Pasta de Destino:").place(x=10, y=50)
pasta_entry = tk.Entry(root, width=50)
pasta_entry.place(x=120, y=50)
tk.Button(root, text="Selecionar Pasta", command=selecionar_pasta).place(x=500, y=45)

# Área de log/status
tk.Label(root, text="Log").place(x=10, y=90)
log_text = scrolledtext.ScrolledText(root, width=70, height=10)
log_text.place(x=120, y=90)

# Botão para iniciar o download
tk.Button(root, text="Download", width=15, command=baixar_video_twitter).place(x=370, y=270)

# Botão para fechar a aplicação
tk.Button(root, text="Fechar", width=15, command=fechar_aplicacao).place(x=500, y=270)

root.mainloop()
