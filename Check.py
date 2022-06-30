from PIL import Image #pip install Pillow
import urllib.request
urllib.request.urlretrieve(
  'https://raw.githubusercontent.com/CheckPlease123/Surprise/main/bla.jpg',"th.png")
IMG = 'th.png' 
WIDTH = 150 
HEIGHT = 80 
OUTPUT = 'output5.txt' 
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-+~<>i!lI;:,\"^`'. ") 
def get_char(r,g,b,alpha = 256): 
    if alpha == 0:
        return ' ' 
    length = len(ascii_char) 
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (255.0 + 1)/length
    return ascii_char[int(gray/unit)] 
im = Image.open(IMG) 
im = im.resize((WIDTH,HEIGHT), Image.NEAREST) 
txt = "" 
for i in range(HEIGHT):
    for j in range(WIDTH):
        txt += get_char(*im.getpixel((j,i)))
    txt += '\n'
print(txt)
with open(OUTPUT,'w') as f: 
    f.write(txt)