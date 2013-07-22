from __future__ import print_function
from wand.image import Image

header_file = 'header.png'
footer_file = 'footer.png'
screen_file = raw_input('What screen (png) to process?: ') + '.png'

header_image = Image(filename=header_file)
footer_image = Image(filename=footer_file)
screen_image = Image(filename=screen_file)

comp_header = 0
comp_footer = screen_image.height - footer_image.height

screen_image.composite(header_image, 0, comp_header)
screen_image.composite(footer_image, 0, comp_footer)

# Export appended image comp
screen_image.save(filename='comp.png')