import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def read_img(img_path):
    img = cv2.imread(img_path)

    if img is None:
        raise FileNotFoundError(f"Nie udało się wczytać obrazu: {img_path}")

    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_processed = cv2.adaptiveThreshold(img_grey, 255,
                                          cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                          cv2.THRESH_BINARY, 11, 2)

    txt = pytesseract.image_to_string(img_processed, lang='eng')

    return txt
