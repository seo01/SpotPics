from common_colors import *
import os, sys

#first argument is the input second is the output html
file_or_dir_in = sys.argv[1]
file_out = sys.argv[2]

files_in = []
if(os.path.isdir(file_or_dir_in)):
    files_in = ['%s/%s' %(file_or_dir_in,f) for f in os.listdir(file_or_dir_in)]
else:
    files_in.append(file_or_dir_in)

file_out = open(file_out,'w')

file_out.write("<html><head>%s</head><body>"%get_common_colors_css())

for path in files_in:
    try:
        colors = get_common_colors_from_path(path)
        if colors:
            file_out.write("<div title='%s'>%s</div>"%(path,get_common_colors_div(colors)))
    except IOError:
        pass
file_out.write("</body></html>")
file_out.close()