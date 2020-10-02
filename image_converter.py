from PIL import Image
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input_dir", help="path to xml file, folder or image (defined by --imageFormat) containing information images")
parser.add_argument("--output_dir", required=True, help="where to put output files")
a = parser.parse_args()

def main():
    if not os.path.exists(a.output_dir):
        os.mkdir(a.output_dir)

    cnt = 1
    for f in os.listdir(a.input_dir):
        if not (f.endswith(".jpg") or f.endswith("DS_Store")):
            img = Image.open(os.path.join(a.input_dir, f))
            img = img.convert('RGB')
            img.save(os.path.join(a.output_dir, f"{cnt}.jpg"), quality=100)
            cnt += 1

main()