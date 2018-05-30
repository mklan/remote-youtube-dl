# remote-youtube-dl
Download youtube videos to your server/NAS/local machine using a simple HTTP GET request

## Setup

```bash
python setup.py install
```

optionally set environment variables to configure the service

```bash
export YDL_DL_PATH='/path/to/downloads' # defaults to the current dir (ommit the trailing '/' !)
export YDL_USE_AUTH='True' # defaults to False
export YDL_HASHED_KEY='yourHashedKey' # mandatory if YDL_USE_AUTH is set to 'True'
```

### Generate hash for authentication

if you set `YDL_USE_AUTH='True'` you need to generate a hash for your auth key by running the following python script:

```python

>>> from pbkdf2 import crypt
>>> crypt('yourKey')

```

the result needs to be exported as the `YDL_HASHED_KEY` environment variable

## Development

```bash
FLASK_APP=src/flask_app.py flask run
```

`http://localhost:5000/ydl?key=<YOUR_KEY>&id=<YOUTUBE_VIDEO_ID>&onlyAudio=True`

key is only mandatory if `YDL_USE_AUTH='True'` 
onlyAudio is optional and defaults to `False`

## Deployment as cgi and lighttpd

```bash
lighttpd -D -f lighttpd.conf
```

> Note: in the deployment case all three environment variables must be set! If you know how to do it conditionally, please make a pull request

`http://localhost:5000/src/app.cgi/ydl?key=<YOUR_KEY>&id=<YOUTUBE_VIDEO_ID>&onlyAudio=True`
