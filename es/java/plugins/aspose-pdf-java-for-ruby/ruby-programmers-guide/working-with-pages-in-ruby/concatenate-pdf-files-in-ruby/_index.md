---
title: Concatenar archivos PDF en Ruby
linktitle: Concatenar archivos PDF en Ruby
type: docs
weight: 10
url: /es/java/concatenate-pdf-files-in-ruby/
description: Combine varios PDFs en un solo documento usando Ruby y Aspose.PDF de manera eficiente.
lastmod: "2026-09-29"
---
## Aspose.PDF - concatenar archivos PDF

Para concatenar archivos PDF usando **Aspose.PDF Java for Ruby**, simplemente invoque el módulo **ConcatenatePdfFiles**.

Código Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf1 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Open the source document

pdf2 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input2.pdf')

# Add the pages of the source document to the target document

pdf1.getPages().add(pdf2.getPages())

# Save the concatenated output file (the target document)

pdf1.save(data_dir+ "Concatenate_output.pdf")

puts "New document has been saved, please check the output file"
```

## Descargar código en ejecución

Descargar **Concatenate PDF Files (Aspose.PDF)** desde cualquier de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/concatenatepdffiles.rb)
