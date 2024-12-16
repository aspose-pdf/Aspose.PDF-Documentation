---
title: Convertir PDF a formato SVG en Ruby
type: docs
weight: 50
url: /es/java/convert-pdf-to-svg-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Convertir PDF a SVG

Para convertir PDF al formato SVG usando **Aspose.PDF Java para Ruby**, simplemente invoca el módulo **PdfToSvg**.

Código Ruby

```java

# La ruta al directorio de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abre el documento objetivo

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# instancia un objeto de SvgSaveOptions

save_options = Rjb::import('com.aspose.pdf.SvgSaveOptions').new

# no comprimir la imagen SVG en un archivo Zip

save_options.CompressOutputToZipArchive = false

# Guardar la salida en formato XLS

pdf.save(data_dir + "Output.svg", save_options)

puts "El documento ha sido convertido exitosamente"
```

## Descargar Código en Ejecución

Descarga **Convertir PDF a formato SVG (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftosvg.rb)