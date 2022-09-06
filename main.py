from module.ext import PDFExtracter
from module.checker import Checker
from module.checker import pdf_from_dir


if __name__ == '__main__':
    dir_path = 'static/'
    check, pdf_files = pdf_from_dir(dir_path)

    if check:
        control_text = ['Order', '21', '1231231', '5612', '66333', 'Car', 'Normal', '1222', 'Careful', '10']

        # init_tesseract()
        pdfEtxractor = PDFExtracter()
        checker = Checker()

        for filename in pdf_files:
            file_path = '/'.join((dir_path, filename))
            ext_data = pdfEtxractor.extract(file_path)

            print(f'\n\n[+] FILE {filename}:')
            print(f'\t{ext_data = }')

            for ctrl_text in control_text:
                checked = checker.check(ctrl_text, ext_data)
                filtred_data = checker.fdata

                print(f'\n\t{ctrl_text = }')
                print(f'\t{checked = }')
                print(f'\t{filtred_data = }')
