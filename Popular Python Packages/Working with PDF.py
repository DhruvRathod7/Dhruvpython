import PyPDF2
with open("first.pdf", "rb") as file:
    reader = PyPDF2.pdfFileReader(file)
    print(reader.numPages)
    page = reader.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPages(page)
    with open("rotated.pdf", "wb") as output:
        writer.write(output)

        merger = PyPDF2.PdfFileMerger()
        file_name = ["first.pdf", "second.pdf"]
        for file_name in file_name:
            merger.append(file_name)
            merger.write("combined.pdf")
