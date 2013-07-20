from __future__ import print_function
from wand.image import Image
from wand.sequence import Sequence

header_file = 'header.png'
footer_file = 'footer.png'
screen_file = raw_input('What screen to process?: ')

header_image = Image(filename=header_file)
footer_image = Image(filename=footer_file)
screen_image = Image(filename=screen_file)

# Get the dimensions of the rectangle to keep
crop_left = 0
crop_top = header_image.height + 1
crop_right = footer_image.width
crop_bottom = screen_image.height - footer_image.height

# Do the crop to keep area not covered by header.png or footer.png
screen_image.crop(crop_left,crop_top,crop_right,crop_bottom)

# Save the preserved area just for debugging
screen_image.save(filename='middle.png')

# Combine header, screen and footer into one image
squish_image = Sequence(header_image)
squish_image.append(screen_image)

# Export appended image comp
header_image.save(filename='squished.png')