import youtube_dl


def youtube_download(youtubeId, ydl_opts):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        # try:
        ydl.download(['http://www.youtube.com/watch?v='+youtubeId])
        # TODO exception does not work due to async shizzle
        # except Exception as error:
