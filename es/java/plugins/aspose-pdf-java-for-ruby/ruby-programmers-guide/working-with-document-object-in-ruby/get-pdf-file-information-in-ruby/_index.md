---
title: Obtener información de archivos PDF en Ruby
linktitle: Obtener información de archivos PDF en Ruby
type: docs
weight: 50
url: /java/get-pdf-file-information-in-ruby/
description: Extraiga metadatos y detalles de archivos PDF mediante programación utilizando Aspose.PDF en Ruby.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Obtener información del archivo PDF



Para obtener información del archivo de un documento PDF usando **Aspose.PDF Java para Ruby**, simplemente invoque el módulo **GetPdfFileInfo**.

Código Rubí


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Get document information

doc_info = doc.getInfo()

# Show document information

puts "Author:-" + doc_info.getAuthor().to_s

puts "Creation Date:-" + doc_info.getCreationDate().to_string

puts "Keywords:-" + doc_info.getKeywords().to_s

puts "Modify Date:-" + doc_info.getModDate().to_string

puts "Subject:-" + doc_info.getSubject().to_s

puts "Title:-" + doc_info.getTitle().to_s
```

## 
Descargar código de ejecución



DescargarВ **Obtener información del archivo PDF (Aspose.PDF)**В de cualquiera de los sitios de codificación social mencionados a continuación:


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getpdffileinfo.rb)
