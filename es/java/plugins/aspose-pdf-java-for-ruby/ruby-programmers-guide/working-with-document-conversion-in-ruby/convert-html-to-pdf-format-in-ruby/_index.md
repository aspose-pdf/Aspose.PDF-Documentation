---
title: Convertir HTML a formato PDF en Ruby
linktitle: Convertir HTML a formato PDF en Ruby
type: docs
weight: 10
url: /java/convert-html-to-pdf-format-in-ruby/
description: Aprenda cómo convertir contenido HTML a formato PDF en Ruby usando Aspose.PDF para generar documentos confiables y precisos.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Convertir HTML a formato PDF



Para convertir HTML a formato PDF usando **Aspose.PDF Java para Ruby**, simplemente invoque el módulo **HtmlToPdf**.

Código Rubí


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

htmloptions = Rjb::import('com.aspose.pdf.HtmlLoadOptions').new(data_dir)

# Load HTML file

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + "index.html", htmloptions)

# Save the concatenated output file (the target document)

pdf.save(data_dir + "html.pdf")

puts "Document has been converted successfully"
```

## 
Descargar código de ejecución



DescargarВ **Convertir HTML a formato PDF (Aspose.PDF)**В desde cualquiera de los sitios de codificación social mencionados a continuación:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/htmltopdf.rb)
