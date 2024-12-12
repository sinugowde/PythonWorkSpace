# pip install pdf2docx

from pdf2docx import Converter
pdf_file = 'Website Hosting.pdf'
docx_file = 'Website Hosting.docx'
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()