#  Convert/VideoToGif - Nexss PROGRAMMER 2.0.0 - Python 3

from moviepy.editor import VideoFileClip

import json
import sys
import os

# STDIN
NexssStdin = sys.stdin.read()

parsedJson = json.loads(NexssStdin)
if 'file' not in parsedJson:
    raise Exception('Attribute `file` is needed as video source.')

path = parsedJson['file']
resultFilename, _ = os.path.splitext(path)
parsedJson["resultFile"] = parsedJson["cwd"] + "/" + resultFilename + '.gif'

print("Writing gif..")
video = (VideoFileClip(parsedJson['cwd'] + "/" + path, audio=False).resize(2))

if 'fps' not in parsedJson:
    fps = 4
else:
    fps = parsedJson["fps"]

if isinstance("fps", int):
    raise Exception('Attribute `fps` must be a number')

# composition = CompositeVideoClip([video]).speedx(0.2)
video.write_gif(parsedJson["resultFile"], fps=fps, fuzz=3)

NexssStdout = json.JSONEncoder().encode(parsedJson)
# STDOUT
sys.stdout.write(NexssStdout)
