from PIL import Image

import fitz
import io


class _Singleton(object):
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance


class _PDFManager(_Singleton):
    def _check_is_scan(self, file_path):
        self.doc = fitz.open(file_path)
        text = ""
        for page in self.doc:
            text += page.get_text()
        return text or None

    def _text_format(self, text):
        text_splines = text.splitlines()
        # text_stspaces = map(lambda el: el.strip(), text_splines)
        # text_seq = tuple(filter(lambda el: el != '', text_stspaces))
        text_output = ' '.join(text_splines)
        return text_output

    def _extract_image(self):
        nps = self.doc.page_count
        for np in range(nps):
            page = self.doc.load_page(np)
            pix = page.get_pixmap()
            pix_bytes = pix.pil_tobytes(format="JPEG")
            stream = io.BytesIO(pix_bytes)
            img = Image.open(stream)
            yield img