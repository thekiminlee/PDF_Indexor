from PyPDF2 import PdfFileReader, PdfFileWriter
import sys
import os

path = "/Users/kimin/Desktop/"
start_page = int(sys.argv[3])
end_page = int(sys.argv[4])


def indexPDF():
    filename, export_file =sys.argv[1], sys.argv[2]
    export_path = os.path.join(path, export_file)

    reader = PdfFileReader(open(filename, 'rb'))
    printer = PdfFileWriter()

    for page in range(start_page-1, end_page-1):
        print(page)
        printer.addPage(reader.getPage(page))


    with open(export_path, 'wb') as pdf:
        printer.write(pdf)


if __name__ == '__main__':
    indexPDF()
