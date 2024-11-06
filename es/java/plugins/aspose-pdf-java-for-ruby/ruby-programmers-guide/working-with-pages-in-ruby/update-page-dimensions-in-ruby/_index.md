---
title: Actualizar Dimensiones de Página en Ruby
type: docs
weight: 90
url: es/java/update-page-dimensions-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Actualizar Dimensiones de Página

Para actualizar las dimensiones de la página usando **Aspose.PDF Java para Ruby**, simplemente invoque el módulo **UpdatePageDimensions**.

Código Ruby

```java

# La ruta al directorio de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abrir el documento objetivo

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# obtener la colección de páginas

page_collection = pdf.getPages()

# obtener una página en particular

pdf_page = page_collection.get_Item(1)

# establecer el tamaño de la página como A4 (11.7 x 8.3 in) y en Aspose.PDF, 1 pulgada = 72 puntos

# por lo que las dimensiones de A4 en puntos serán (842.4, 597.6)

pdf_page.setPageSize(597.6,842.4)

# guardar el archivo PDF recién generado

pdf.save(data_dir + "output.pdf")

puts "¡Dimensiones actualizadas exitosamente!"
```

## Descargar Código en Ejecución

Descargar **Update Page Dimensions (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/updatepagedimensions.rb)