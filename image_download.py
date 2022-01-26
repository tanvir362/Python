import requests
from PIL import Image

from io import StringIO, BytesIO

r = requests.get('https://cdn.pixabay.com/photo/2021/09/15/15/48/seals-6627197_960_720.jpg')
print(type(r.content))
img = Image.open(BytesIO(r.content))
img.save('./images/downloaded_image.jpg')