import pdftotext
from pdf2image import convert_from_path
import PIL
import os
from tqdm import tqdm
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

input = 'Batch_1'
output = 'issues'
input_file = os.listdir(input)

for file in tqdm(input_file):
    # print(file)
    input_path = os.path.join(input,file)                                       # 输入路径
    output_path = os.path.join(output,file.replace('.pdf','.txt'))              # 输出路径
    # print(input_path)
    content = ''
    print(input_path)# 记录转换内容的空白string
    with open(input_path, "rb") as f:
        pdf = pdftotext.PDF(f)                                                  # 先使用pdf2txt转换pdf
    images = convert_from_path(input_path)                                  # pdf2image 转换每页pdf为pil图像文件
    with open(output_path, 'w', encoding='utf-8') as f:
        for img in images:
            f.write(pytesseract.image_to_string(img, config='--psm 4 -c preserve_interword_spaces=1'))     # 使用 pytesseract 转换pil图像文件为文字
