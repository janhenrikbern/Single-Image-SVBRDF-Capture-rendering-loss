from PIL import Image
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input_dir", help="path to xml file, folder or image (defined by --imageFormat) containing information images")
parser.add_argument("--output_dir", required=True, help="where to put output files")
a = parser.parse_args()

def main():
    if not os.path.exists(a.output_dir):
        pwd = ""
        for path_segment in a.output_dir.split('/'):
            pwd = os.path.join(pwd, path_segment)
            if not os.path.exists(pwd):
                os.mkdir(pwd)

    cnt = 1
    queue = [a.input_dir]
    while queue:
        pwd = queue.pop(0)
        for f in os.listdir(pwd):
            if f.endswith("DS_Store"): continue
            f_path = os.path.join(pwd, f)
            if os.path.isdir(f_path):
                queue.append(f_path)
            elif os.path.isfile(f_path) and not f.endswith(".jpg"):
                img = Image.open(f_path)
                img = img.convert('RGB')
                w, h = img.size
                if not (h ==256 and w ==256):
                    ratio =  256 / min(h,w)
                    img = img.resize((round(w*ratio)+1, round(h*ratio)+1))
                    img = img.crop((0,0,256,256))
                img.save(os.path.join(a.output_dir, f"{cnt}.jpg"), quality=100)
                cnt += 1

main()