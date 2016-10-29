#!/usr/bin/env python

import requests


def download_file(url):
    '''Function

    Downloads a file using the requests library

    '''

    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    res = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in res.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
    return local_filename

URL = 'https://vine.co/Blanketsburg/likes?mode=list'
download_file(URL)
