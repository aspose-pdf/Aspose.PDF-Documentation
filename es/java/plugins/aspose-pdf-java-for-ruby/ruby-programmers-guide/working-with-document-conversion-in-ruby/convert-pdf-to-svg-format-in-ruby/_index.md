---
title: Convertir PDF a formato SVG en Ruby
linktitle: Convertir PDF a formato SVG en Ruby
type: docs
weight: 50
url: /es/java/convert-pdf-to-svg-format-in-ruby/
description: Descubra cómo convertir archivos PDF a formato SVG usando Ruby y Aspose.PDF, habilitando gráficos vectoriales escalables y editables.
lastmod: "2026-09-03"
---
## Aspose.PDF - Convertir PDF a SVG

Para convertir PDF a formato SVG usando **Aspose.PDF Java for Ruby**, simplemente invoque el módulo **PdfToSvg**.

Código Ruby

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

## Descargar Código en Ejecución

DescargarВ **Convertir PDF a formato SVG (Aspose.PDF)**В deВ cualquier de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftosvg.rb)
