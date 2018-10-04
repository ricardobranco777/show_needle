#!/usr/bin/env python3
"This script draws the rectangles described by http://open.qa/docs/#_areas"

import re
import json
import sys

from PIL import Image, ImageDraw

COLORS = {'match': 'green', 'exclude': 'red', 'ocr': 'orange'}


def main():
    "Main function"
    if len(sys.argv) != 2:
        print("Usage: %s NEEDLE[.json|png]" % sys.argv[0], file=sys.stderr)
        sys.exit(1)

    needle = re.sub(r"\.(png|json)$", "", sys.argv[1])

    image = Image.open(needle + ".png").convert('RGBA')
    draw = ImageDraw.Draw(image)

    with open(needle + ".json") as file:
        data = json.load(file)

    # Draw rectangles
    for item in (_ for _ in data['area']):
        draw.rectangle(
            ((item['xpos'], item['ypos']),
             (item['xpos'] + item['width'], item['ypos'] + item['height'])),
            outline=COLORS[item['type']])

    del draw
    image.show()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
