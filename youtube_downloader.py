from pytube import YouTube
from pytube import Playlist
def downloadVideos(links, save_path):
    
    if type(links) == 'str':
        links = list(links)
        
    index_length = len(str(len(links)))

    for i in range(len(links)):
        index = "Lecture " + ("0"*(index_length-len(str(i+1)))) + str(i+1) + " "
        try: 
            # object creation using YouTube 
            yt = YouTube(links[i]) 
        except: 
            #to handle exception 
            print("Connection Error in Lecture: " + index)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download(output_path = save_path, filename_prefix=index)

        
def downloadPlaylist(playlist, save_path):
    urls = Playlist(playlist)
    index_length = len(str(len(urls)))
    for url_index in range(len(urls)):
        index = "Lecture " + ("0"*(index_length-len(str(url_index+1)))) + str(url_index+1) + " "
        try:
            yt = YouTube(urls[url_index])
        except:
            print("Error occured in Lecture: " + index)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download(output_path = save_path, filename_prefix=index)