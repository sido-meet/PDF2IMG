import fitz
import os

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
    else:
        pass

def pdf_image(pdfPath, img_output_dir, zoom_x, zoom_y, rotation_angle):
    """
    :param pdfPath: pdf文件的路径
    :param img_output_dir: 图像要保存的文件夹
    :param zoom_x: x方向的缩放系数
    :param zoom_y: y方向的缩放系数
    :param rotation_angle: 旋转角度
    :return: None
    """
    # 打开PDF文件
    pdf = fitz.open(pdfPath)
    name = pdf.name
    name = name.split('/')[-1].split('.')[0]
    print(f"开始处理文件: {name}")
    # 逐页读取PDF
    for pg in range(0, pdf.page_count):
        page = pdf[pg]
        # 设置缩放和旋转系数    
        trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotation_angle)
        pm = page.get_pixmap(matrix=trans, alpha=False)
        # 开始写图像
        mkdir(img_output_dir + name)
        pm.save(img_output_dir + name + '/' + str(pg + 1) + ".png")
        print("第{}页处理完成".format(pg + 1))
    pdf.close()

pdf_file_dir = "pdfs/"
img_output_dir = "images/"
assert os.path.exists(pdf_file_dir), "pdf dir not exist, please create a dir name 'pdfs'"
if not os.path.exists(img_output_dir):
    os.makedirs(img_output_dir)

files = os.listdir(pdf_file_dir)
pdf_files_path = [os.path.join(pdf_file_dir, f) for f in files if f.lower().endswith(".pdf")]

print(f"开始处理，共{len(pdf_files_path)}个pdf文件")
for pdf in pdf_files_path:
    pdf_image(pdf, img_output_dir, 20, 20, 0)

input("处理结束!\nPress any key to exit...")

