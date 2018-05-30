from __future__ import unicode_literals
import os

from flask import Flask
from flask import request
from flask import jsonify

from pbkdf2 import crypt

from src.services.downloader import youtube_download

app = Flask(__name__)

HASHED_KEY = os.environ.get('YDL_HASHED_KEY', None)
USE_AUTH = os.environ.get('YDL_USE_AUTH', False)
DL_PATH = os.environ.get('YDL_DL_PATH', '.')


@app.route("/", methods=["GET"])
def handle_index():
    return handle_help()


@app.route("/ydl", methods=["GET"])
def handle_download():

    youtubeId = request.args.get('id')
    onlyAudio = request.args.get('onlyAudio')
    key = request.args.get('key')

    if not youtubeId:
        return handle_help(400)

    # Authentication
    if USE_AUTH and not HASHED_KEY == crypt(key, HASHED_KEY):
        return response(500, 'incorrect key')

    ydl_opts = {
        'format': 'bestaudio' if onlyAudio else 'best',
        'outtmpl': DL_PATH+'/%(title)s.%(ext)s'
    }

    youtube_download(youtubeId, ydl_opts)
    return response(200, 'download started...')


@app.route("/help", methods=["GET"])
def handle_help(code=200):
    return response(code, 'how to use this service:  /ydl?id=<YOUTUBE_ID>&key=<YOUR_SECRET_KEY>onlyAudio=false')


def response(code, message):
    response = jsonify({'message': message})
    response.status_code = code
    return response
