from __future__ import print_function
from wand.image import Image
import glob

# Set all possible partials to a 1x1px transparent PNG.
header_image = Image(filename='_empty.png')
footer_image = Image(filename='_empty.png')
leftrail = Image(filename='_empty.png')
rightrail = Image(filename='_empty.png')

# Get all PNGs in the current directory
files = glob.glob('*.png')

# Function used for printing the names of the partial files we found
def partials_used(file):
	print("Partial used: " + file)

for file in files:

	# Check to see if the current file is a partial or a screen
	if ( file == "_header.png" ):
		header_image = Image(filename='_header.png')
		partials_used(file)
	elif ( file == "_footer.png" ):
		footer_image = Image(filename='_footer.png')
		partials_used(file)
	elif ( file == "_leftrail.png" ):
		partials_used(file)
	elif ( file == "_rightrail.png" ):
		partials_used(file)
	else:
		# Make a Wand object from our current file
		screen_image = Image(filename=file)
		# Coordinates for where we composite
		comp_header = 0
		comp_footer = screen_image.height - footer_image.height
		# Do the compositing of header and footer onto the screen image
		screen_image.composite(header_image, 0, comp_header)
		screen_image.composite(footer_image, 0, comp_footer)
		# Export appended image comp
		screen_image.save(filename=file)
