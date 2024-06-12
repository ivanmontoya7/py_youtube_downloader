from pytube import YouTube

x=input("video/audio\n")
url=input("pega el enlace:\n")
yt = YouTube(url)
print("Titulo: ", yt.title)

if (x=="audio"):
     yd = yt.streams.get_audio_only().download()
     print("Descarga completada")

if(x=="video"):
    yt.streams.get_highest_resolution().download()
    print("Descarga completada")