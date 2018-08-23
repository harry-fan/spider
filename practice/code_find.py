# coding:utf-8

# 验证码识别，需要安装下面的包
# tesseract-ocr   sudo apt-get name
# pytesseract     pip install
# pillow          pip install 

import pytesseract
from PIL import Image

image = Image.open('code.png')
pytesseract.tesseract_cmd = 'tesseract.exe'
code = pytesseract.image_to_string(image)

print(code)
