import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def img2str(img) -> str:
    return pytesseract.image_to_string(img, lang='rus')
