from ._kernel import _Singleton
from ._kernel import _PDFManager

import pytesseract


# only for Windows OS
def init_tesseract(tes_path=r'C:\Program Files\Tesseract-OCR\tesseract'):
    pytesseract.pytesseract.tesseract_cmd = tes_path


class PDFExtracter(_PDFManager):
    def _extract_non_searchable(self):
        text_data = ''
        for stream in self._extract_image():
            text_data += pytesseract.image_to_string(stream)
            text_formated = self._text_format(text_data)
        return text_formated

    def _extract_searchable(self):
        text_data = self._text_format(self.text_or_none)
        return text_data

    def extract(self, file_path):
        self.text_or_none = self._check_is_scan(file_path)
        if self.text_or_none:
            return self._extract_searchable()
        else:
            return self._extract_non_searchable()
