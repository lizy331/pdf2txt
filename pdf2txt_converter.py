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

input = 'issues'
output = 'issues'
input_file = os.listdir(input)

for file in tqdm(input_file):
    # print(file)
    input_path = os.path.join(input,file)                                       # 输入路径
    output_path = os.path.join(output,file.replace('.pdf','.txt'))              # 输出路径
    print(input_path)
    content = ''
    with open(input_path, "rb") as f:
        pdf = pdftotext.PDF(f)                                                  # 先使用pdf2txt转换pdf
    for page in pdf:
        content += page
    if len(content) > 10:                                                       # 若果记录内容长度大于10 pdf为文字类型
        with open(output_path,'w',encoding='utf-8') as w:
            w.write(content)
    else:                                                                       # 否则 pdf为图像类型
        # print(input_path)  # 记录转换内容的空白string
        images = convert_from_path(input_path)                                  # pdf2image 转换每页pdf为pil图像文件
        with open(output_path, 'w', encoding='utf-8') as f:
            for img in images:
                f.write(pytesseract.image_to_string(img, config='--psm 4'))     # 使用 pytesseract 转换pil图像文件为文字



