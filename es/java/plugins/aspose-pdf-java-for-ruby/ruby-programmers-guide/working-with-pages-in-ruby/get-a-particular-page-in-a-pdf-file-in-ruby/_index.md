---
title: Obtener una Página Particular en un Archivo PDF en Ruby
type: docs
weight: 30
url: /es/java/get-a-particular-page-in-a-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obtener Página

Para obtener una Página Particular en un documento PDF usando **Aspose.PDF Java para Ruby**, simplemente invoca el módulo **GetPage**.

Código Ruby

```java
# La ruta al directorio de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abrir el documento objetivo

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# obtener la página en el índice particular de la Colección de Páginas

pdf_page = pdf.getPages().get_Item(1)

# crear un nuevo objeto Documento

new_document = Rjb::import('com.aspose.pdf.Document').new

# agregar página a la colección de páginas del nuevo objeto documento

new_document.getPages().add(pdf_page)

# guardar el archivo PDF recién generado

new_document.save(data_dir + "output.pdf")

puts "¡Proceso completado con éxito!"
```

## Descargar Código en Ejecución

Descargar **Obtener Página (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getpage.rb)