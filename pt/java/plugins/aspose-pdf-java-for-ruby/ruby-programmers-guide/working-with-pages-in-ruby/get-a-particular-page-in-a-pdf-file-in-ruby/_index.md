---
title: Obtenha uma página específica em um arquivo PDF em Ruby
linktitle: Obtenha uma página específica em um arquivo PDF em Ruby
type: docs
weight: 30
url: /java/get-a-particular-page-in-a-pdf-file-in-ruby/
description: Acesse e manipule páginas individuais em documentos PDF usando Ruby e Aspose.PDF.
lastmod: "2026-06-09"
---
## Aspose.PDF - Obter página

Para obter uma página específica em um documento PDF usando **Aspose.PDF Java para Ruby**, basta invocar o módulo **GetPage**.

Código Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# get the page at particular index of Page Collection

pdf_page = pdf.getPages().get_Item(1)

# create a new Document object

new_document = Rjb::import('com.aspose.pdf.Document').new

# add page to pages collection of new document object

new_document.getPages().add(pdf_page)

# save the newly generated PDF file

new_document.save(data_dir + "output.pdf")

puts "Process completed successfully!"
```

## Baixar código em execução

Baixe **Get Page (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getpage.rb)
