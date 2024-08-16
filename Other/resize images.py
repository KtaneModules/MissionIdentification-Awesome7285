from PIL import Image
import os

folder = r"F:\New Computer\Unity\MISSION IMAGES/Raw/"
out = r"F:\New Computer\Unity\MISSION IMAGES/Resized/"

for img in os.listdir(folder):
    im = Image.open(folder+img)
    im = im.resize((im.width//2, im.height//2))
    im.save(out+img)