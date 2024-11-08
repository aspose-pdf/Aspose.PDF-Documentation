---
title: Insertar una Página Vacía al Final del Archivo PDF en Ruby
type: docs
weight: 60
url: /es/java/insert-an-empty-page-at-end-of-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Insertar una Página Vacía al Final del Archivo PDF

Para insertar una página vacía al final del documento PDF usando **Aspose.PDF Java para Ruby**, simplemente invoque el módulo **InsertEmptyPageAtEndOfFile**.

Código Ruby

```java
# La ruta al directorio de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abrir el documento objetivo

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# insertar una página vacía en un PDF

pdf.getPages().add()

# Guardar el archivo de salida concatenado (el documento objetivo)

pdf.save(data_dir+ "output.pdf")

puts "¡Página vacía añadida con éxito!"
```

## Descargar Código en Ejecución

Descargar **Insertar una Página Vacía al Final del Archivo PDF (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypageatendoffile.rb)