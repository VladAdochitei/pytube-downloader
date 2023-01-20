from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    video = youtubeObject.streams.get_highest_resolution()

    try:
        video.download()
    except:
        print("Download failed, check internet connection")
        return 1

    print ("Download completed!")    

link = input("Insert Youtube link: ")
Download(link)