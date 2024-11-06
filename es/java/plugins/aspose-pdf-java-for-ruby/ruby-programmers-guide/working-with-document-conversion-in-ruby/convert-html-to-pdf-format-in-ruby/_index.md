---
title: Convertir HTML a Formato PDF en Ruby
type: docs
weight: 10
url: es/java/convert-html-to-pdf-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Convertir HTML a Formato PDF

Para convertir HTML a formato PDF usando **Aspose.PDF Java para Ruby**, simplemente invoque el módulo **HtmlToPdf**.

Código Ruby

```java

# La ruta al directorio de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

htmloptions = Rjb::import('com.aspose.pdf.HtmlLoadOptions').new(data_dir)

# Cargar archivo HTML

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + "index.html", htmloptions)

# Guardar el archivo de salida concatenado (el documento objetivo)

pdf.save(data_dir + "html.pdf")

puts "El documento ha sido convertido exitosamente"
```

## Descargar Código en Ejecución

Descargue **Convertir HTML a Formato PDF (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/htmltopdf.rb)