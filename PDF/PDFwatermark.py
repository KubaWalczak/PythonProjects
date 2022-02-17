import PyPDF2


def watermarker():

    path = 'C:/Users/Kuba/PycharmProjects/pythonProject/PDF/pliki'

    writer = PyPDF2.PdfFileWriter()
    #mam watermarka
    template = PyPDF2.PdfFileReader(f'{path}/super.pdf')


    #mam plik do watermarkowania
    watermark = PyPDF2.PdfFileReader(f'{path}/wtr.pdf')


    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page2 = watermark.getPage(0)
        page.mergePage(page2)
        writer.addPage(page)
    # merger = PyPDF2.pdf.PageObject(page)  # ok
    # merger2 = PyPDF2.pdf.PageObject(page2)
    # #
    # merger.mergePage(merger2)

        with open('pliki/super2.pdf', 'wb') as f:
            writer.write(f)

watermarker()