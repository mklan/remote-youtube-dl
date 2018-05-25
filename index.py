from __future__ import unicode_literals

from flask import Flask
from flask import request
from flask import jsonify

import youtube_dl

app = Flask(__name__)

@app.route("/", methods=["GET"])
def handle_index():
    return handle_help()

@app.route("/ydl", methods=["GET"])
def handle_download():

    id = request.args.get('id')
    onlyAudio = request.args.get('onlyAudio')

    if not id:
        return handle_help(400)

    ydl_opts = {
        'format': 'bestaudio' if onlyAudio else 'best',
        'outtmpl' : '~/Videos/%(title)s.%(ext)s' #TODO this needs to be configurable
    }

    youtube_download(id, ydl_opts)
    return response(200, 'download started...')

@app.route("/help", methods=["GET"])
def handle_help(code = 200):
    return response(code, 'provide an id argument with a value of a youtube video id and an optional boolean flag onlyAudio')




def youtube_download(id, ydl_opts):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download(['https://www.youtube.com/watch?v='+id])
        except Exception as error:
            #TODO an error if the video was not found needs to be thrown, this does not work right now
            return response(500, 'error')


def response(code, message):
    response = jsonify({'message': message})
    response.status_code = code
    return response
