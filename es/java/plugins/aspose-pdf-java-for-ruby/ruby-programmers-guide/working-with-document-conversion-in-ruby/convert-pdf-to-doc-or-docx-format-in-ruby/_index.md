---
title: Convertir PDF a formato DOC o DOCX en Ruby
linktitle: Convertir PDF a formato DOC o DOCX en Ruby
type: docs
weight: 30
url: /es/java/convert-pdf-to-doc-or-docx-format-in-ruby/
description: Aprenda cómo convertir documentos PDF a formatos DOC o DOCX en Ruby con Aspose.PDF, lo que permite una edición y procesamiento más fáciles.
lastmod: "2026-09-03"
---
## Aspose.PDF - Convertir PDF a DOC o DOCX

Para convertir un documento PDF a formato DOC o DOCX usando **Aspose.PDF Java for Ruby**, simplemente invoque el módulo **PdfToDoc**.

Código Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Save the concatenated output file (the target document)

pdf.save(data_dir + "output.doc")

puts "Document has been converted successfully"
```

## Descargar código en ejecución

Descargar\u0412\u00A0**Convertir PDF a DOC o DOCX (Aspose.PDF)**\u0412\u00A0de\u0412\u00A0cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftodoc.rb)
