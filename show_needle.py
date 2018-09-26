#!/usr/bin/env python3
"This script draws the rectangles described by http://open.qa/docs/#_areas"

import re
import json
import sys

import matplotlib.pyplot as plt
from matplotlib import patches

from PIL import Image

import numpy as np

COLORS = {'match': 'green', 'exclude': 'red', 'ocr': 'orange'}


def main():
    "Main function"
    if len(sys.argv) != 2:
        print("Usage: %s NEEDLE[.json|png]", file=sys.stderr)
        sys.exit(1)

    needle = re.sub(r"\.(png|json)$", "", sys.argv[1])

    image = np.array(Image.open(needle + ".png"), dtype=np.uint8)

    # Create figure and axes
    _, axes = plt.subplots(1)

    # Display the image
    axes.imshow(image)

    with open(needle + ".json") as file:
        data = json.load(file)

    # Draw rectangles
    for item in (_ for _ in data['area']):
        # Create a Rectangle patch
        rect = patches.Rectangle(
            (item['xpos'], item['ypos']), item['width'], item['height'],
            linewidth=1, edgecolor=COLORS[item['type']], facecolor='none')
        # Add the patch to the Axes
        axes.add_patch(rect)

    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
