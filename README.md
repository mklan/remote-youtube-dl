# remote-youtube-dl
Download youtube videos to your server or NAS

## Setup

```bash
python setup.py install
```

set environment variables to configure the service

```bash
export YDL_DL_PATH='/path/to/downloads' # defaults to the current dir (ommit the trailing '/' !)
export USE_AUTH='True' # defaults to False
export HASHED_KEY='yourHashedKey' # mandatory if USE_AUTH is set to 'True'
```

### Generate Hash for Authentication

if you set `USE_AUTH='True'` you need to generate a hash for your auth key by running the following python script:

```python

>>> from pbkdf2 import crypt
>>> crypt('yourKey')

```

the result needs to be exported as the `HASHED_KEY` environment variable

## Usage

```bash
FLASK_APP=__init__.py flask run
```

`http://localhost:5000/ydl?key=<YOUR_KEY>&id=<YOUTUBE_VIDEO_ID>&onlyAudio=True`

key is only mandatory if `USE_AUTH='True'` 
onlyAudio is optional and defaults to `False`
