# import module

import from pdf2image convert_from_path

pages = convert_from_path('example.pdf')

for i in the range(len(pages)):

pages[i].save('page'+ str(i) +'.jpg', 'JPEG')
