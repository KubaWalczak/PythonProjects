import sys
import os
from PIL import Image

# path = sys.argv[1]
# directory = sys.argv[2]
#
#
#
# for filename in os.listdir(path):
#     clean_name = os.path.splitext(filename)[0]
#     img = Image.open(f'{path}{filename}')
#     # added the / in case user doesn't enter it. You may want to check for this and add or remover it.
#     img.save(f'{directory}/{clean_name}.png', 'png')
#     print('all done!')



from PIL import Image, ImageFilter
import os
import sys
file = r'\Users\Kuba\PycharmProjects\pythonProject\practice images'
file_PNG = r'\Users\Kuba\PycharmProjects\pythonProject\practice images\PNG'

if not os.path.exists(file_PNG):
    os.makedirs(file_PNG)
def converter():
    with open(file) as infile:
        for image in infile:
            f, e = os.path.splitext(image)
            outfile = f + ".jpg"
# converter()
# # #
# def converter():
#
#     file = r'\Users\Kuba\PycharmProjects\pythonProject\practice images'
#     file_PNG = r'\Users\Kuba\PycharmProjects\pythonProject\practice images\PNG'
#
#     # assert os.path.isfile(path)
#     # with open(path, "r") as a:
#     #     pass
#     for image in os.listdir(file):
#             new_img = Image.open(f'{file}/{image}')
#             clean = os.path.splitext(image)
#             new_img.save(f'{clean}.png')


converter()
#
#
#
#
#
# # img = Image.open('./pratice images')
# # new_image = img.resize((400,400))
# # new_image.save('./pratice images/PNG/astro_small.png', )