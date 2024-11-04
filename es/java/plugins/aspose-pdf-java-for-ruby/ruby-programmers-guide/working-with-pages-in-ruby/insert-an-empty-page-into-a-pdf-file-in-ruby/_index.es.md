---
title: Insertar una Página Vacía en un Archivo PDF en Ruby
type: docs
weight: 70
url: /java/insert-an-empty-page-into-a-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Insertar una Página Vacía

Para insertar una página vacía en un documento PDF usando **Aspose.PDF Java para Ruby**, simplemente invoca el módulo **InsertEmptyPage**.

Código Ruby

```java

# La ruta al directorio de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abrir el documento de destino

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# insertar una página vacía en un PDF

pdf.getPages().insert(1)

# Guardar el archivo de salida concatenado (el documento de destino)

pdf.save(data_dir+ "output.pdf")

puts "¡Página vacía añadida exitosamente!"
```

## Descargar Código en Ejecución

Descargar **Insertar una Página Vacía (Aspose.PDF)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypage.rb)