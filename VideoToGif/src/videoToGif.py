#  Convert/VideoToGif - Nexss PROGRAMMER 2.0.0 - Python 3

from moviepy.editor import VideoFileClip


import platform
import json
import sys
import os

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
# STDIN
NexssStdin = sys.stdin.read()

parsedJson = json.loads(NexssStdin)
if 'file' not in parsedJson:
    # Don't! If you catch, likely to hide bugs.
    raise Exception('Attribute `file` is needed as video source.')

path = parsedJson['file']
resultFilename, _ = os.path.splitext(path)
parsedJson["resultFile"] = parsedJson["cwd"] + "/" + resultFilename + '.gif'

print("Writing gif..")
video = (VideoFileClip(parsedJson['cwd'] + "/" + path, audio=False).resize(2))

# parsedJson.fps = video.fps
# parsedJson.duration = video.duration

# composition = CompositeVideoClip([video]).speedx(0.2)
video.write_gif(parsedJson["resultFile"], fps=4, fuzz=3)

NexssStdout = json.JSONEncoder().encode(parsedJson)
# STDOUT
sys.stdout.write(NexssStdout)
