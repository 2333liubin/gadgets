"""
    convert the separated audio and video (.m4s) into one complete
    file (.mp4) from mobile phone, for Bilibili, which are stored
    in folder '/Android/data/tv.danmaku.bili/download'

    copy and put that folder in the same path with this program, and
    following codes will use pre-installed 'ffmpeg.exe' to complete
    the conversion
"""

import os
import pdb
import subprocess

def combineAudioVideo(DownloadPath):

    os.makedirs('output_convert_bili_to_mp4', exist_ok=True)

    for root, dirs, _ in os.walk(DownloadPath, topdown=True):
        for curDir in dirs:
            for subDir in os.listdir(os.path.join(root, curDir)):
                _audio = os.path.join(root, curDir, subDir, '80', 'audio.m4s')
                _video = os.path.join(root, curDir, subDir, '80', 'video.m4s')
                # pdb.set_trace()

                subprocess.Popen(
                    'ffmpeg -i %s -i %s -codec copy %s' % (
                        _video,
                        _audio,
                        os.path.join('output_convert_bili_to_mp4', curDir+'.mp4')
                    ),
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT,
                    shell=False,
                )

    print('convert to mp4 for bili finished!')


if __name__=='__main__':
    combineAudioVideo('download')