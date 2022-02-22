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

for path in files_in:
    try:
        colors = get_common_colors_from_path(path)
        if colors:
            file_out.write("%s\n"%(get_common_colors_generated_sol(colors, os.path.basename(path).split('.')[0])))
    except IOError:
        pass
file_out.close()