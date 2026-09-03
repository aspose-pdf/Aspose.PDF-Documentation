---
title: Concatenar archivos PDF en Ruby
linktitle: Concatenar archivos PDF en Ruby
type: docs
weight: 10
url: /java/concatenate-pdf-files-in-ruby/
description: Combine varios archivos PDF en un solo documento utilizando Ruby y Aspose.PDF de manera eficiente.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Concatenar archivos PDF



Para concatenar archivos PDF usando **Aspose.PDF Java para Ruby**, simplemente invoque el módulo **ConcatenatePdfFiles**.

Código Rubí


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

## 
Descargar código de ejecución



Descargue **Concatenar archivos PDF (Aspose.PDF)**В desde cualquiera de los sitios de codificación social mencionados a continuación:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/concatenatepdffiles.rb)
