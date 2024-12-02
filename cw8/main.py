import os
from cw8.read_img import read_img

base_dir = os.path.dirname(__file__)
img_path = [
    os.path.join(base_dir, 'images/img1.jpeg'),
    os.path.join(base_dir, 'images/img2.jpeg'),
    os.path.join(base_dir, 'images/img3.jpeg'),
    os.path.join(base_dir, 'images/img4.jpeg'),
    os.path.join(base_dir, 'images/img5.jpeg')
]

for path in img_path:
    try:
        txt = read_img(path)
        print(f'Tekst z {path}:\n{txt}\n')
    except FileNotFoundError as e:
        print(e)
