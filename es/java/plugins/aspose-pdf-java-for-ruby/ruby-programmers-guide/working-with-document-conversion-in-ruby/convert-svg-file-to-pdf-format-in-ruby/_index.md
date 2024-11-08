---
title: Convertir archivo SVG a formato PDF en Ruby
type: docs
weight: 60
url: /es/java/convert-svg-file-to-pdf-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Convertir SVG a PDF

Para convertir un archivo SVG a formato PDF usando **Aspose.PDF Java para Ruby**, simplemente invoca el módulo **SvgToPdf**.

Código Ruby

```java

# La ruta al directorio de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instanciar objeto LoadOption usando la opción de carga SVG

options = Rjb::import('com.aspose.pdf.SvgLoadOptions').new

# Crear objeto de documento

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'Example.svg', options)

# Guardar la salida en formato XLS

pdf.save(data_dir + "SVG.pdf")

puts "El documento se ha convertido con éxito"
```

## Descargar Código en Ejecución

Descarga **Convertir SVG a PDF (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/svgtopdf.rb)