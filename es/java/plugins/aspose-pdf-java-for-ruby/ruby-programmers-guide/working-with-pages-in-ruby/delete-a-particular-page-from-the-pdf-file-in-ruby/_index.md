---
title: Eliminar una Página Particular del Archivo PDF en Ruby
type: docs
weight: 20
url: /es/java/delete-a-particular-page-from-the-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Eliminar Página

Para eliminar una página particular del documento PDF usando **Aspose.PDF Java para Ruby**, simplemente invoca el módulo **DeletePage**.

Código Ruby

```java
# La ruta al directorio de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abrir el documento objetivo

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# eliminar una página particular

pdf.getPages().delete(2)

# guardar el archivo PDF recién generado

pdf.save(data_dir + "output.pdf")

puts "¡Página eliminada exitosamente!"
```

## Descargar Código en Ejecución

Descarga **Eliminar Página (Aspose.PDF)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/deletepage.rb)