"""
    download music (.mp3) from netease platform
"""

import os
import requests


def downloadSongFromNetease(url):

    os.makedirs('output_download_netease_song', exist_ok=True)

    _id = url.split('id=')[-1]
    _newUrl = 'http://music.163.com/song/media/outer/url?id=%s.mp3' % _id
    _resp = requests.get(_newUrl, timeout=5)

    if _resp.content is None or _resp.content == b'':
        print('download song id = {%s} failed!' % _id)
    else:
        with open(os.path.join('output_download_netease_song', str(_id)+'.mp3'), 'wb') as f:
            f.write(_resp.content)
        print('download song id = {%s} success!' % _id)

if __name__=='__main__':
    downloadSongFromNetease('https://music.163.com/#/song?id=2115904437')