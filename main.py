from module.ext import PDFExtracter
from module.checker import Checker
from module.checker import pdf_from_dir


if __name__ == '__main__':
    dir_path = 'static'
    # check, pdf_files = pdf_from_dir(dir_path)
    filename = 'some.pdf'
    file_path = '/'.join((dir_path, filename))
    
    control_text = ['stranda 6200']

    pdfEtxractor = PDFExtracter()
    checker = Checker()

    ext_data = pdfEtxractor.extract(file_path)

    print(f'\n\n[+] FILE {filename}:')
    print(f'\t{ext_data = }')

    for ctrl_text in control_text:
        checked = checker.check(ctrl_text, ext_data)

        print(f'\n\t{ctrl_text = }')
        print(f'\t{checked = }')
