from pytube import YouTube

link = input("Enter the link of video you want to download: ")
yt = YouTube(link)


print("Title: ",yt.title)

print("No of Views: ",yt.views)

print("Length: ",yt.length)

print("Rating: ",yt.rating)

for stream in yt.streams:
    print(stream) 
      

av = input(str("Do you want to download audio or video? "))

if av == "audio":
    print(yt.streams.filter(only_audio=True))
else:
    print(yt.streams.filter(only_video=True))

tag = input("Input the tag no of the quality you want: ")
ys = yt.streams.get_by_itag(tag)

print("Downloading................")
ys.download("C:/Users/APMC/Downloads")
print("Download completed!!!!!!!")
