from pytube import YouTube, Playlist

def baixa_vid(url):
    youtube = YouTube(url)

    youtube.streams.get_highest_resolution().download()

def baixa_pl(url):
    playlist = Playlist(url)

    for video in playlist:
        youtube = YouTube(video)
        youtube.streams.get_highest_resolution().download()


print('Bem vindo ao Dowloader de vídeos do Youtube feito em Python!')
i = input('Digite 1 se deseja baixar um vídeo ou 2 se deseja baixar uma playlist => ')

if i=='1':
    print('*VIDEO*')
    url = input('Copie e cole a URL do vídeo que deseja baixar e aperte ENTER => ')
    baixa_vid(url)
if i=='2':
    print('*PLAYLIST*')
    pl_url = input('Copie e cole a URL da playlist que deseja baixar e aperte ENTER => ')
    baixa_pl(pl_url)
