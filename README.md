compbot 0.1
------------

A super simple CLI utility for updating headers and footers on design composites to keep your stakeholder happy.

## Requirements

`mkvirtualenv compbot`
`brew install imagemagick1
`pip install Wand`

## Usage

Throw compbot.py into the folder with all of the comps to be updated. Make sure you have a `_header.png` and a `_footer.png` file to go along with whatever other PNGs you need to update.

`python compbot.py` and all PNGs other than the _header and _footer will be updated. Now move the screens into your project management tool.

## Assumptions

Currently this is a super basic script and assumes all of your comps are PNGs.