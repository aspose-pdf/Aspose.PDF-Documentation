---
title: Convertir archivos SVG a formato PDF en Ruby
linktitle: Convertir archivos SVG a formato PDF en Ruby
type: docs
weight: 60
url: /java/convert-svg-file-to-pdf-format-in-ruby/
description: Aprenda a convertir archivos SVG a formato PDF en Ruby usando Aspose.PDF para una transformación de documentos precisa y escalable.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Convertir SVG a PDF



Para convertir un archivo SVG a formato PDF usando **Aspose.PDF Java para Ruby**, simplemente invoque el módulo **SvgToPdf**.

Código Rubí


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instantiate LoadOption object using SVG load option

options = Rjb::import('com.aspose.pdf.SvgLoadOptions').new

# Create document object

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'Example.svg', options)

# Save the output to XLS format

pdf.save(data_dir + "SVG.pdf")

puts "Document has been converted successfully"
```

## 
Descargar código de ejecución



Descargue **Convierta SVG a PDF (Aspose.PDF)**В desde cualquiera de los sitios de codificación social mencionados a continuación:


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/svgtopdf.rb)
