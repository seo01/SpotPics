from common_colors import *
import os, sys
#First argument is the image, second is the SVG

file_in = sys.argv[1]
file_out = sys.argv[2]

file_out = open(file_out,'w')

file_out.write('<?xml version="1.0" standalone="no"?>\n'+ \
    '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">')

colors = get_common_colors_from_path(file_in)
if colors:
    try:
        file_out.write(get_common_colors_svg(colors))
    except IOError:
        pass
file_out.close()