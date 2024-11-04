---
title: Concatenate archivos PDF en Ruby
type: docs
weight: 10
url: /java/concatenate-pdf-files-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Concatenar Archivos PDF

Para concatenar archivos PDF usando **Aspose.PDF Java para Ruby**, simplemente invoque el módulo **ConcatenatePdfFiles**.

Código Ruby

```java
# La ruta al directorio de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abrir el documento de destino

pdf1 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Abrir el documento de origen

pdf2 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input2.pdf')

# Agregar las páginas del documento de origen al documento de destino

pdf1.getPages().add(pdf2.getPages())

# Guardar el archivo de salida concatenado (el documento de destino)

pdf1.save(data_dir+ "Concatenate_output.pdf")

puts "El nuevo documento ha sido guardado, por favor revise el archivo de salida"
```

## Descargar Código en Ejecución

Descargue **Concatenate PDF Files (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/concatenatepdffiles.rb)