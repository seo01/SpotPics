from PIL import Image, ImageDraw
import math
from operator import itemgetter

def get_common_colors_from_path(path):
    img = Image.open(path).convert('RGB')
    return get_common_colors_from_image(img)
    
def get_common_colors_from_image(img):
    colors = img.getcolors(1000000)
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
        reduct = (int(int(color[0]/div)*div),int(int(color[1]/div)*div),int(int(color[2]/div)*div))
        new_colors[reduct]=new_colors.get(reduct,0)+freq
    new_colors = [(freq,color) for (color,freq) in new_colors.items()]
    return new_colors

def dampen_frequencies(colors):
    return  [(int(math.pow(freq,0.25)),color) for (freq,color) in colors]

def normalise_freq(colors,splits=16):
    new_colors = []
    colors = dampen_frequencies(colors)
    total = sum([freq for (freq,color) in colors])
    ex = 0
    for (freq,color) in colors:
        norm = int((freq*splits+ex)/total)
        ex = int((freq*splits+ex)%total)
        new_colors.append((norm,color))
    #correction
    total = sum([freq for (freq,color) in new_colors[:-1]])
    if new_colors:
        new_colors[-1]=(splits-total,new_colors[-1][1])
    return new_colors

def only_first_monochrome(colors):
    new_colors = []
    has_monochrome = False
    for (freq,color) in colors:
        monochrome = is_monochrome(color)
        if not has_monochrome:
            new_colors.append((freq,color))
        if monochrome:
            has_monochrome = True
        else:
            new_colors.append((freq,color))
    return new_colors

def is_monochrome(color):
    return max(color) - min(color) < 50

def select_common_colors(colors):
    colors = sorted(colors,key=itemgetter(0))
    colors.reverse()
    colors = only_first_monochrome(colors)
    popular = colors[:4]
    popular =  normalise_freq(popular)
    return popular

#for web page generation
def get_common_colors_css():
    return "<style>.circle{border-radius: 50%;display: inline-block;	margin-right: 2px; margin-bottom:2px; width:20px;height:20px} .grid{float:left;margin-right:15px}</style>"

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
    svg = '<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="100" height="100" viewBox="0 0 100 100">'
    count = 0
    print(colors)
    for (freq,color) in colors:
        for i in range(int(freq)):
            row = int(count % 4)
            col = int(count / 4)
            c = 'rgb(%s,%s,%s)' % color
            svg += '<circle cx="%s" cy="%s" r="10" fill="%s"/>'% (25*row+12,25*col+12,c)
            count += 1
    svg += '</svg> '
    return svg

def get_common_colors_generated_sol(colors, label):
    colors4 = [(0,[0,0,0]),(0,[0,0,0]),(0,[0,0,0]),(0,[0,0,0])]
    for i in range(len(colors)):
        colors4[i] = colors[i]
    color_str = ",".join(["[%s,%s,%s,%s]" % (freq, color[0], color[1], color[2]) for (freq, color) in colors4])
    sol = """     mint(
            /*colors=*/
            ["""
    sol = sol+color_str
    sol = sol+"""],
            /*token=*/
            \""""
    sol = sol+label
    sol = sol+"""\"
        );"""
    return sol