import os
from cw8.read_img import read_img


base_dir = os.path.dirname(__file__)
img_paths = [
    os.path.join(base_dir, 'images/img1.jpeg'),
    os.path.join(base_dir, 'images/img2.jpeg'),
    os.path.join(base_dir, 'images/img3.jpeg'),
    os.path.join(base_dir, 'images/img4.jpeg'),
    os.path.join(base_dir, 'images/img5.jpeg')
]

for img_path in img_paths:
    try:
        results = read_img(img_path)
        print(f"Obraz: {img_path}")
        for method, text in results.items():
            print(f"\nMetoda: {method}\nOCR Tekst:\n{text}\n")
    except FileNotFoundError as e:
        print(e)
