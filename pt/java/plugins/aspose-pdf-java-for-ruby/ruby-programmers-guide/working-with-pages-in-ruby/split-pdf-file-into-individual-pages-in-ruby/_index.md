---
title: Divida o arquivo PDF em páginas individuais em Ruby
linktitle: Divida o arquivo PDF em páginas individuais em Ruby
type: docs
weight: 80
url: /java/split-pdf-file-into-individual-pages-in-ruby/
description: Entenda como dividir um arquivo PDF em páginas individuais com Ruby e Aspose.PDF, facilitando o gerenciamento e a extração de conteúdo.
lastmod: "2026-06-09"
---
## Aspose.PDF - Dividir páginas

Para dividir um documento PDF em páginas individuais usando **Aspose.PDF Java para Ruby**, basta invocar o módulo **SplitAllPages**.

Código Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# loop through all the pages

pdf_page = 1

#for (int pdfPage = 1; pdfPage<= pdfDocument1.getPages().size(); pdfPage++)

while pdf_page <= pdf.getPages().size()

# create a new Document object

new_document = Rjb::import('com.aspose.pdf.Document').new

# get the page at particular index of Page Collection

new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# save the newly generated PDF file

new_document.save(data_dir + "page_#{pdf_page}.pdf")

pdf_page +=1

end

puts "Split process completed successfully!"
```

## Baixar código em execução

Baixe **Split Pages (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/splitallpages.rb)
