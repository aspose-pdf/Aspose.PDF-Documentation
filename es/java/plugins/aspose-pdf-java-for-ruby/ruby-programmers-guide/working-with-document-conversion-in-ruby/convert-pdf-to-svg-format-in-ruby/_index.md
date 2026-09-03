---
title: Convertir PDF a formato SVG en Ruby
linktitle: Convertir PDF a formato SVG en Ruby
type: docs
weight: 50
url: /java/convert-pdf-to-svg-format-in-ruby/
description: Descubra cómo convertir archivos PDF a formato SVG usando Ruby y Aspose.PDF, lo que permite gráficos vectoriales escalables y editables.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Convertir PDF a SVG



Para convertir PDF a formato SVG usando **Aspose.PDF Java para Ruby**, simplemente invoque el módulo **PdfToSvg**.

Código Rubí


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# instantiate an object of SvgSaveOptions

save_options = Rjb::import('com.aspose.pdf.SvgSaveOptions').new

# do not compress SVG image to Zip archive

save_options.CompressOutputToZipArchive = false

# Save the output to XLS format

pdf.save(data_dir + "Output.svg", save_options)

puts "Document has been converted successfully"
```

## 
Descargar código de ejecución



Descargue **Convierta PDF a formato SVG (Aspose.PDF)**В desde cualquiera de los sitios de codificación social mencionados a continuación:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftosvg.rb)
