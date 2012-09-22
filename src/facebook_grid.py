from common_colors import *
import os, sys,csv

#THIS IS AN EXPERIMENTAL SCRIPT LOOKING AT THE CHANGE IN FACEBOOK'S HOME PAGE COLOURS OVER TIME
#SEE THE RESULTS IN THE EXAMPLES FOLDER

file_out = sys.argv[2]

dates = ["2012-01-02","2012-01-25","2012-02-01","2012-02-13","2012-02-25","2012-03-01","2012-03-10","2012-03-22","2012-04-10","2012-05-01","2012-06-01","2012-07-01","2012-09-01"]

files_in = [('facebook.com',sys.argv[1]+'/%s/imgs/facebook.com-clipped.png'%date) for date in dates]

file_out = open(file_out,'w')

file_out.write("<html><head>%s</head><body>"%get_common_colors_css())

for (site,path) in files_in:
    try:
        colors = get_common_colors_from_path(path)
        if colors:
            file_out.write("<a href='http://%s' title='%s'>%s</a>"%(site,site,get_common_colors_div(colors)))
    except IOError:
        pass
file_out.write("</body></html>")
file_out.close()