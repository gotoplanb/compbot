from __future__ import print_function
from wand.image import Image
import glob

header_image = Image(filename='_header.png')
footer_image = Image(filename='_footer.png')

# Get all PNGs in the current directory
files = glob.glob('*.png')

# Pop the first two items because they are the _header and _footer
files.pop(0)
files.pop(0)

for file in files:

	screen_image = Image(filename=file)

	# Coordinates for where we composite
	comp_header = 0
	comp_footer = screen_image.height - footer_image.height

	# Do the compositing of header and footer onto the screen image
	screen_image.composite(header_image, 0, comp_header)
	screen_image.composite(footer_image, 0, comp_footer)

	# Export appended image comp
	screen_image.save(filename=file)