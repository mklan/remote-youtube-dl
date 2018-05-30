import cgi
import cgitb
import os

from src.services.downloader import youtube_download
from pbkdf2 import crypt

cgitb.enable()  # Optional; for debugging only

HASHED_KEY = os.environ.get('YDL_HASHED_KEY', None)
USE_AUTH = os.environ.get('YDL_USE_AUTH', False)
DL_PATH = os.environ.get('YDL_DL_PATH', '.')


def execute():
    print('haa')
    arguments = cgi.FieldStorage()

    youtubeId = arguments['id']
    onlyAudio = arguments['onlyAudio']
    key = arguments['key']

    if USE_AUTH and not HASHED_KEY == crypt(key, HASHED_KEY):
        print('auth failed: Authentication is active and a wrong key was provided')

    ydl_opts = {
        'format': 'bestaudio' if onlyAudio else 'best',
        'outtmpl': DL_PATH+'/%(title)s.%(ext)s'
    }

    youtube_download(youtubeId, ydl_opts)
    print("download started")
