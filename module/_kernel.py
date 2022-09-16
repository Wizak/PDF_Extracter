from PIL import Image

import PyPDF2


class _Singleton(object):
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance


class _PDFManager:
    def _check_is_scan(self, file_path):
        pdf_reader = PyPDF2.PdfReader(file_path)
        self.general_page = pdf_reader.pages[0]
        return self.general_page.extractText() == ''

    def _prettify_text(self, text):
        text_splines = text.splitlines()
        text_stspaces = map(lambda el: el.strip(), text_splines)
        text_sspaces = tuple(filter(lambda el: el != '', text_stspaces))[1:]
        joined = ' '.join(text_sspaces)
        return joined

    def _extract_image(self):
        x_object = self.general_page["/Resources"]["/XObject"].getObject()

        for obj in x_object:
            if x_object[obj]["/Subtype"] == "/Image":
                size = (x_object[obj]["/Width"], x_object[obj]["/Height"])
                data = x_object[obj].getData()

                if x_object[obj]["/ColorSpace"] == "/DeviceRGB":
                    mode = "RGB"
                else:
                    mode = "P"

                if x_object[obj]["/Filter"] == "/FlateDecode":
                    img = Image.frombytes(mode, size, data)
                    return img
                if x_object[obj]["/Filter"] == "/DCTDecode" or x_object[obj]["/Filter"] == "/JPXDecode":
                    return data
