import fitz
import pytesseract
from PIL import Image
import io

path = "static/test.pdf"


def check():
    text = ""
    doc = fitz.open(path)
    for page in doc:
        text += page.get_text()
    return text


def read_scan():
    doc = fitz.open(path)
    nps = doc.page_count
    for np in range(nps):
        page = doc.load_page(np)
        pix = page.get_pixmap()
        pix_bytes = pix.pil_tobytes(format="JPEG")
        stream = io.BytesIO(pix_bytes)
        img = Image.open(stream)
        yield img
    

def main():
    text = check()
    if text == '' or len(text) <= 5:
        stream = read_scan()
        scan_text = ''
        for image in stream:
            scan_text += pytesseract.image_to_string(image)
            print(scan_text)
    else:
        print(text)


if __name__ == '__main__':
    main()
