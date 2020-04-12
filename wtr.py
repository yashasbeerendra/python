import PyPDF2
import sys

import PyPDF2
import sys


page1 = PyPDF2.PdfFileReader(open('original.pdf', 'rb'))
page2 = PyPDF2.PdfFileReader(open('original (1).pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

page = page1.getPage(0)
page.mergePage(page2.getPage(0))
output.addPage(page)

output.write(open('me.pdf', 'wb'))
