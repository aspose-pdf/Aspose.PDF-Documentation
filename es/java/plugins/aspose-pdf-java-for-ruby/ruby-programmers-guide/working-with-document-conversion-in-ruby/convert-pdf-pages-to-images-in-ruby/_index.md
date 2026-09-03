---
title: Convertir páginas PDF a imágenes en Ruby
linktitle: Convertir páginas PDF a imágenes en Ruby
type: docs
weight: 20
url: /es/java/convert-pdf-pages-to-images-in-ruby/
description: Descubra cómo convertir páginas PDF en imágenes usando Ruby con Aspose.PDF, facilitando la extracción de contenido visual de los PDFs.
lastmod: "2026-09-03"
---
## Aspose.PDF - Convertir páginas PDF a imágenes

Para convertir todas las páginas de un documento PDF a imágenes usando **Aspose.PDF Java for Ruby**, simplemente invoque el módulo **ConvertPagesToImages**.

Código Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

converter = Rjb::import('com.aspose.pdf.facades.PdfConverter').new

converter.bindPdf(data_dir + 'input1.pdf')

converter.doConvert()

suffix = ".jpg"

image_count = 1

image_format_internal = Rjb::import('com.aspose.pdf.ImageFormatInternal')

while converter.hasNextImage()

В В В  converter.getNextImage(data_dir + "image#{image_count}#{suffix}", image_format_internal.getJpeg())

В В В  image_count +=1

end

puts "PDF pages are converted to individual images successfully!"
```

## Descargar código en ejecución

DescargarВ **Convert PDF pages to Images (Aspose.PDF)**В desdeВ cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/convertpagestoimages.rb)
