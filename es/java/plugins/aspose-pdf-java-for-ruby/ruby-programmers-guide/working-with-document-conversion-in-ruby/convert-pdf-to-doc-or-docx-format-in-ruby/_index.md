---
title: Convertir PDF a formato DOC o DOCX en Ruby
type: docs
weight: 30
url: es/java/convert-pdf-to-doc-or-docx-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Convertir PDF a DOC o DOCX

Para convertir un documento PDF a formato DOC o DOCX usando **Aspose.PDF Java para Ruby**, simplemente invoca el módulo **PdfToDoc**.

Código Ruby

```java

# La ruta al directorio de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abre el documento objetivo

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Guarda el archivo de salida concatenado (el documento objetivo)

pdf.save(data_dir + "output.doc")

puts "El documento ha sido convertido exitosamente"
```

## Descargar Código en Ejecución

Descargar **Convertir PDF a DOC o DOCX (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftodoc.rb)