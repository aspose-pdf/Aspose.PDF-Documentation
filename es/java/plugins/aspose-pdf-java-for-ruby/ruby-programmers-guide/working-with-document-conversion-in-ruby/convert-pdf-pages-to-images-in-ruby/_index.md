---
title: Convertir páginas de PDF a Imágenes en Ruby
type: docs
weight: 20
url: es/java/convert-pdf-pages-to-images-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Convertir páginas de PDF a Imágenes

Para convertir todas las Páginas a Imágenes de un documento PDF usando **Aspose.PDF Java para Ruby**, simplemente invoca el módulo **ConvertPagesToImages**.

Código Ruby

```java

# La ruta al directorio de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

converter = Rjb::import('com.aspose.pdf.facades.PdfConverter').new

converter.bindPdf(data_dir + 'input1.pdf')

converter.doConvert()

suffix = ".jpg"

image_count = 1

image_format_internal = Rjb::import('com.aspose.pdf.ImageFormatInternal')

while converter.hasNextImage()

    converter.getNextImage(data_dir + "image#{image_count}#{suffix}", image_format_internal.getJpeg())

    image_count +=1

end

puts "¡Las páginas del PDF se han convertido en imágenes individuales con éxito!"
```

## Descargar Código en Ejecución

Descarga **Convertir páginas de PDF a Imágenes (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/convertpagestoimages.rb)