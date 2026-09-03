---
title: Establecer información del archivo PDF en Ruby
linktitle: Establecer información del archivo PDF en Ruby
type: docs
weight: 120
url: /es/java/set-pdf-file-information-in-ruby/
description: Definir y actualizar programáticamente los metadatos del PDF como título, autor y palabras clave usando Ruby.
lastmod: "2026-09-03"
---
## Aspose.PDF - Establecer información del archivo PDF

Para actualizar la información del documento PDF usando **Aspose.PDF Java for Ruby**, simplemente invoque el módulo **SetPdfFileInfo**.

Código Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Get document information

doc_info = doc.getInfo()

doc_info.setAuthor("Aspose.PDF for java")

doc_info.setCreationDate(Rjb::import('java.util.Date').new)

doc_info.setKeywords("Aspose.PDF, DOM, API")

doc_info.setModDate(Rjb::import('java.util.Date').new)

doc_info.setSubject("PDF Information")

doc_info.setTitle("Setting PDF Document Information")

# save update document with new information

doc.save(data_dir + "Updated_Information.pdf")

puts "Update document information, please check output file."
```

## Descargar código en ejecución

DescargarВ **Establecer información de archivo PDF (Aspose.PDF)**В deВ cualquier sitio de codificación social mencionado a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setpdffileinfo.rb)
