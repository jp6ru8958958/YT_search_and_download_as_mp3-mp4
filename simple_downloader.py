
import youtube_dl

def Mp3_download(video_url):
    mp4_opts = {
        'format': 'bestaudio',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320'
        }]
    }
    with youtube_dl.YoutubeDL(mp4_opts) as ydl:
        ydl.download([video_url])
    print("MP4 file have downloaded")


def Mp4_download(video_url):
    mp3_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]'
    }
    with youtube_dl.YoutubeDL(mp3_opts) as ydl:
        ydl.download([video_url])
    print("MP3 file have downloaded")


def main():
    video_url = "https://www.youtube.com/watch?v=bxbXUMy4kok"
    user_input = input("MP3/MP4")
    if user_input == "MP3" or "Mp3" or "mp3" or "mP3":
        Mp3_download(video_url)
    elif user_input == "MP4" or "Mp4" or "mp4" or "mP4":
        Mp4_download(video_url)


if __name__ == "__main__":
    main()
