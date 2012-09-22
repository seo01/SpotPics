import Image, ImageDraw, math
from operator import itemgetter

def get_common_colors_from_path(path):
    img = Image.open(path)
    return get_common_colors_from_image(img)
    
def get_common_colors_from_image(img):
    colors = img.getcolors(250000)
    if not colors:
        return None
    colors = group_colors(colors,None)
    colors = filter_pale_colors(colors)
    colors = select_common_colors(colors)
    return colors
    

def filter_pale_colors(colors):
    return [(freq,color) for (freq,color) in colors if sum(color[0:3])<600]#896

def calculate_divisions(l):
    return int(math.pow(2,math.log(l,10)))/2+1 if l else 4

def group_colors(colors,div=4):
    if not div:
        div = calculate_divisions(len(colors))
    new_colors = {}
    for (freq,color) in colors:
        reduct = ((color[0]/div)*div,(color[1]/div)*div,(color[2]/div)*div)
        new_colors[reduct]=new_colors.get(reduct,0)+freq
    new_colors = [(freq,color) for (color,freq) in new_colors.iteritems()]
    return new_colors

def dampen_frequencies(colors):
    return  [(int(math.pow(freq,0.33)),color) for (freq,color) in colors]

def normalise_freq(colors,splits=16):
    new_colors = []
    colors = dampen_frequencies(colors)
    total = sum([freq for (freq,color) in colors])
    ex = 0
    for (freq,color) in colors:
        norm = (freq*splits+ex)/total
        ex = (freq*splits+ex)%total
        new_colors.append((norm,color))
    #correction
    total = sum([freq for (freq,color) in new_colors[:-1]])
    if new_colors:
        new_colors[-1]=(splits-total,new_colors[-1][1])
    return new_colors

def select_common_colors(colors):
    colors = sorted(colors,key=itemgetter(0))
    colors.reverse()
    popular = colors[:4]
    popular =  normalise_freq(popular)
    return popular

#for web page generation
def get_common_colors_css():
    return "<style>.circle{border-radius: 50%;display: inline-block;	margin-right: 2px; width:20px;height:20px} .grid{float:left;margin-right:15px}</style>"

def get_common_colors_div(colors,grid=True):
    div = ""
    div += "<div class='grid'>"
    count = 0
    for (freq,color) in colors:
        for i in range(freq):
            if grid and count % 4 == 0:
                div+= "<br/>"
            div+= "<div class='circle' style='background-color:rgb(%s,%s,%s)'></div>"%color
            count += 1
    div += "</div>"
    return div

def get_common_colors_svg(colors):
    svg = '<svg xmlns="http://www.w3.org/2000/svg" version="1.1">'
    count = 0
    for (freq,color) in colors:
        for i in range(freq):
            row = count % 4
            col = count / 4
            c = 'rgb(%s,%s,%s)' % color
            svg += '<circle cx="%s" cy="%s" r="10" fill="%s"/>'% (25*row+10,25*col+10,c)
            count += 1
    svg += '</svg> '
    return svg