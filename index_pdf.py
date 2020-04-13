from PyPDF2 import PdfFileReader, PdfFileWriter
import sys


def indexPDF(argv):
    filename, export_path = argv[1], argv[2]
    start_page, end_page = int(argv[3]), int(argv[4])

    reader = PdfFileReader(open(filename, 'rb'))
    printer = PdfFileWriter()

    for page in range(start_page-1, end_page):
        printer.addPage(reader.getPage(page))

    with open(export_path, 'wb') as pdf:
        printer.write(pdf)


if __name__ == '__main__':
    indexPDF(sys.argv)
