#  Convert/toWebP - Nexss PROGRAMMER 2.x
import json
import sys

import os
import string
import numbers

sys.path.append(os.path.join(os.getenv(
    "NEXSS_PACKAGES_PATH"), "Nexss", "Lib"))

from NexssLog import nxsInfo, nxsOk, nxsWarn, nxsError

try:
    from PIL import Image
except ImportError:
    try:
        import Image
    except:
        nxsError("Pillow is not installed. Init command wasn't run? nexss pkg init.")
        sys.exit(1)
        
def convert_to_webp(source, destination, optimize = True, quality = 100):  
    image = Image.open(source) 
    # image = image.convert('RGB')
    image.save(destination, format="webp")  # Convert image to webp

    return destination

# STDIN
NexssStdin = sys.stdin.read()

parsedJson = json.loads(NexssStdin)

if not "nxsIn" in parsedJson.keys():
    parsedJson["error"] = "You need to pass image file to parse."
else:
    
    if not "nxsOut" in parsedJson: # and not isinstance(parsedJson['nxsOut'], list):
        parsedJson['nxsOut'] = []
        
    for fileForWebP in parsedJson['nxsIn']:
        if not ":" + os.path.sep in fileForWebP:
            p = os.path.join(parsedJson["cwd"], fileForWebP)
        else:
            p = fileForWebP

        if not os.path.exists(p):
            nxsError(f'File not found: {p}')
            sys.exit(1)
        
        
        nxsInfo("Converting: "+p)
        resultFile = convert_to_webp(p, os.path.splitext(p)[0]+'.webp')
        
        parsedJson['nxsOut'].append(resultFile)

NexssStdout = json.JSONEncoder().encode(parsedJson)
# STDOUT
sys.stdout.write(NexssStdout)

if not "file" in parsedJson:
    exit(1)