
"""
Patrick McMackin June '22

This is a part of the making of a LaTex cookbook for recipes that
I want to keep track of for personal use. This python script is to 
address that issue that I orignially kept these recipes 
as screenshots of text. Here the images are converted to simple text
using Google's pytesseract. This text is stored in a simple .txt
file and then can be cut into the .tex file for the cookbook.

I'm lazy and didn't want to retype all of them
"""


from PIL import Image
from pytesseract import pytesseract
import glob

if __name__ == "__main__":

    files = glob.glob("*.jpg")+glob.glob("*.png")+glob.glob("*.jpeg")

    text = []
    for f in files:
        text.append(pytesseract.image_to_string(Image.open(f)))

    with open('recipeText.txt', 'w') as f2:
        for line in text:
            f2.write(line[:-1])
            f2.write("\n\n===================================\n")
            f2.write("===================================\n\n")
    f2.close()
