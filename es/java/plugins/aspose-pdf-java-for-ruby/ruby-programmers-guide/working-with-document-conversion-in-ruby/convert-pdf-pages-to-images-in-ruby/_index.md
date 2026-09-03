---
title: Convertir páginas PDF a imágenes en Ruby
linktitle: Convertir páginas PDF a imágenes en Ruby
type: docs
weight: 20
url: /java/convert-pdf-pages-to-images-in-ruby/
description: Descubra cómo convertir páginas PDF en imágenes usando Ruby con Aspose.PDF, lo que facilita la extracción de contenido visual de archivos PDF.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Convierte páginas PDF en imágenes



Para convertir todas las páginas en imágenes de un documento PDF utilizando **Aspose.PDF Java para Ruby**, simplemente invoque el módulo **ConvertPagesToImages**.

Código Rubí


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

## 
Descargar código de ejecución



DescargarВ **Convierta páginas PDF en imágenes (Aspose.PDF)**В desde cualquiera de los sitios de codificación social mencionados a continuación:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/convertpagestoimages.rb)
