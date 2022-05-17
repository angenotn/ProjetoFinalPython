from pafy import *

link = input("URL: ")
print('''Formatos disponiveis: 
[MP3]
[MP4]
Escolha o desejado (Apenas serão aceitas letras maiúsculas!)''')
formato = input("-> ")

if formato == "MP3":
    video = pafy.new(link)
    bestaudio = video.getbestaudio()
    bestaudio.download(f"\\mp3\\{video.title}.mp3")
    print("\033[32m**DOWNLOAD CONCLUÍDO COM SUCESSO!!**\033[m")
    print("\033[36m**O arquivo foi salvo na pasta de destino do formato escolhido!\033[m")
elif formato == "MP4":
    video = pafy.new(link)
    best = video.getbest(preftype="mp4")
    best.download(f"\\mp4\\{video.title}.mp4")
    print("\033[32m**DOWNLOAD CONCLUÍDO COM SUCESSO!!**\033[m") 
    print("\033[36m**O arquivo foi salvo na pasta de destino do formato escolhido!\033[m")
else:
    print("\033[31mFormato INVÁLIDO! Tente novamente!\033[m")
