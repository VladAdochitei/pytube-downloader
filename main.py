from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    
    try:
        youtubeObject.download()
    except:
        print("Download failed, check internet connection")
        return 1

    print ("Download completed!")    

link = input("Insert Youtube link: ")
Download(link)