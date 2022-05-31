from pytube import YouTube

vid = input('Вставьте ссылку на видео, которое хотите скачать: ')
res_video = input('Укажите качество видео (например 360p, 720p, 1080p): ') # например 360p, 720p, 1080p
path = input('Укажите папку для скачивания: ')

myVideoStream = YouTube(vid)
print("Название: " + myVideoStream.title)
print("Продолжительность: " + str(myVideoStream.length)+" сек")
print("Количество просмотров: " + str(myVideoStream.views))
yt = myVideoStream.streams.filter(file_extension = "mp4", resolution = res_video)
yt.first().download(path)


# from pytube import YouTube

# vid = input('Вставьте ссылку на видео, которое хотите скачать: ')
# yt = YouTube(vid)

# path = input('Напишите адрес папки, куда скачать файл: ')
# yt.streams.filter(progressive=True, file_extension='mp4')
# yt.streams.order_by('resolution')
# yt.streams.desc()
# yt.streams.first().download(path)



# from pytube import YouTube
# myVideo = YouTube("https://www.youtube.com/watch?v=OTCuykFHBeA")
# print(myVideo.title) # название видео
# print(myVideo.length) # длина видео (сек)
# print(myVideo.thumbnail_url) # 3. URL-адрес миниатюры
# print(myVideo.description) # описание к видео
# print(myVideo.views) # сколько просмотров
# print(myVideo.rating) # рейтинг
# print(myVideo.age_restricted) # ограничение по возрасту

# Importing YouTube Module from pytube library
# from pytube import YouTube
# # Prompting user for Youtube Video link
# youtube_url = input("Please enter a YouTube link:")
# # Creating YouTube object with the link
# myVideo = YouTube(youtube_url)
# # Title of the Video
# print("Title: " + myVideo.title)
# # Length of the Video in Seconds
# print("Duration: " + str(myVideo.length))
# # URL of the Thumbnail of the video
# print("Thumbnail Link: " + myVideo.thumbnail_url)
# # Description of the Video
# print("Description: " + myVideo.description)
# # Total Views of the Video
# print("Views: " + str(myVideo.views))
# # Age Restricted Content
# print("Age Restricted: " + str(myVideo.age_restricted))
# # ID of the Video
# print("Video ID: " + myVideo.video_id)


#from pytube import YouTube
# yt = YouTube("https://www.youtube.com/watch?v=oS8lASbvlpI")
# myVideoStreams = yt.streams
# print(myVideoStreams)

# myHDStream = YouTube("https://www.youtube.com/watch?v=oS8lASbvlpI").streams.first()
# myAudioStream = YouTube("https://www.youtube.com/watch?v=oS8lASbvlpI").streams.last()


# print(myHDStream)
# print("\n")
# print(myAudioStream)



