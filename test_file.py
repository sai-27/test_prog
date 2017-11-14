from PIL import Image, ImageDraw, ImageFont
import sys

def load_letters(fname):
	im = Image.open(fname)
	print(im)
	px = im.load()
	(x_size, y_size) = im.size
	print(im.size)

f_name = sys.argv[1]
load_letters(f_name)
