import webbrowser
import pyperclip
import sys

if sys.argv.__len__() > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# webbrowser.open('https://google.com/maps/place/' + address)
webbrowser.open('https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=' + address)
