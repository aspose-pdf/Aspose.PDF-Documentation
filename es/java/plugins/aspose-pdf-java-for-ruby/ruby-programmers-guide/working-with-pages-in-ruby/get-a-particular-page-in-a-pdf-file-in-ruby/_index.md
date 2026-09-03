---
title: Obtener una página específica en un archivo PDF en Ruby
linktitle: Obtener una página específica en un archivo PDF en Ruby
type: docs
weight: 30
url: /es/java/get-a-particular-page-in-a-pdf-file-in-ruby/
description: Acceder y manipular páginas individuales en documentos PDF usando Ruby y Aspose.PDF.
lastmod: "2026-09-03"
---
## Aspose.PDF - Obtener página

Para obtener una página específica en un documento PDF usando **Aspose.PDF Java for Ruby**, simplemente invoque el módulo **GetPage**.

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

## Descargar código en ejecución

Descargar **Get Page (Aspose.PDF)**В fromВ cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getpage.rb)
