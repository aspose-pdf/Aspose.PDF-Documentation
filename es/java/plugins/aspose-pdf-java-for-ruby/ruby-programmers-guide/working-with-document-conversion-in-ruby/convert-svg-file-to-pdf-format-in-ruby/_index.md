---
title: Convertir archivo SVG a formato PDF en Ruby
linktitle: Convertir archivo SVG a formato PDF en Ruby
type: docs
weight: 60
url: /es/java/convert-svg-file-to-pdf-format-in-ruby/
description: Aprenda cómo convertir archivos SVG a formato PDF en Ruby usando Aspose.PDF para una transformación de documentos precisa y escalable.
lastmod: "2026-09-03"
---
## Aspose.PDF - Convertir SVG a PDF

Para convertir un archivo SVG a formato PDF usando **Aspose.PDF Java for Ruby**, simplemente invoque el módulo **SvgToPdf**.

Código Ruby

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

## Descargar código en ejecución

Descargar **Convertir SVG a PDF (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/svgtopdf.rb)
