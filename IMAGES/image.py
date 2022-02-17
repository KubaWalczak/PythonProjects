import sys
import os
from PIL import Image

path = r'\Users\Kuba\PycharmProjects\pythonProject\practice images'
directory = r'\Users\Kuba\PycharmProjects\pythonProject\practice images\PNG'



for filename in os.listdir(path):
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(f'{path}{filename}')
    # added the / in case user doesn't enter it. You may want to check for this and add or remover it.
    img.save(f'{directory}/{clean_name}.png', 'png')
    print('all done!')