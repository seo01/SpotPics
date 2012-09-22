from common_colors import *
import os, sys,csv

def read_sites(f):
    reader = csv.reader(open(f,'r'))
    sites = []
    for row in reader:
        sites.append(row[1])
    return sites

def filter_sites(sites):
    #strip sites with the same first bit
    site_parts = {}
    new_sites = []
    for site in sites:
        part = site.split('.')[0]
        if part not in site_parts:
            new_sites.append(site)
        site_parts[part] = True
    return new_sites

#first argument is the data path second is the output html
sites = read_sites(sys.argv[1]+'/alexa/alexa.500')
sites = filter_sites(sites)
file_out = sys.argv[2]

files_in = [(site,sys.argv[1]+'/imgs/%s-clipped.png'%site) for site in sites]

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