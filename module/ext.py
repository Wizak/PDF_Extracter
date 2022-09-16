from ._kernel import _Singleton
from ._kernel import _PDFManager

import pytesseract


# only for Windows OS
def init_tesseract(tes_path=r'C:\Program Files\Tesseract-OCR\tesseract'):
    pytesseract.pytesseract.tesseract_cmd = tes_path


class PDFExtracter(_Singleton, _PDFManager):
    def extract_non_searchable(self):
        image_bytes = self._extract_image()
        img_to_text = pytesseract.image_to_string(image_bytes)
        text_data = self._prettify_text(img_to_text)
        return text_data

    def extract_searchable(self):
        text_to_text = self.general_page.extractText()
        text_data = self._prettify_text(text_to_text)
        return text_data

    def extract(self, file_path):
        check = self._check_is_scan(file_path)
        if check:
            return self.extract_non_searchable()
        else:
            return self.extract_searchable()
