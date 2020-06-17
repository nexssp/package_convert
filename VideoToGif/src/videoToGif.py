#  Convert/VideoToGif - Nexss PROGRAMMER 2.0.0 - Python 3

from moviepy.editor import VideoFileClip

import json
import sys
import os
import string
import numbers

# STDIN
NexssStdin = sys.stdin.read()

parsedJson = json.loads(NexssStdin)

if '_file' not in parsedJson:
    raise Exception('Attribute `_file` is needed as video source.')

path = parsedJson['_file']
resultFilename, _ = os.path.splitext(path)
parsedJson["_resultFile"] = os.path.join(
    parsedJson["cwd"], resultFilename + '.gif')

if '_resize' not in parsedJson:
    resize = .2
else:
    resize = parsedJson["_resize"]

if not isinstance(resize, numbers.Number):
    raise Exception('Attribute `_resize` must be a number')

sys.stderr.write(f'NEXSS/info: Resizing..')

video = (VideoFileClip(os.path.join(
    parsedJson['cwd'], path), audio=False).resize(resize))

if '_fps' not in parsedJson:
    fps = 4
else:
    fps = parsedJson["_fps"]

if not isinstance(fps, numbers.Number):
    raise Exception('Attribute `_fps` must be a number')


# composition = CompositeVideoClip([video]).speedx(0.2)

sys.stderr.write(f'NEXSS/info: Writing Gif..')
video.write_gif(parsedJson["_resultFile"], fps=fps,
                fuzz=3, verbose=False, logger=None)

parsedJson["nxsOut"] = parsedJson["_resultFile"]

NexssStdout = json.JSONEncoder().encode(parsedJson)
# STDOUT
sys.stdout.write(NexssStdout)
