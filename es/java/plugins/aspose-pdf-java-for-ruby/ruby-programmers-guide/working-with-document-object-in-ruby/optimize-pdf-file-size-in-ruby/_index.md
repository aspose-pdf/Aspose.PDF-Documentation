---
title: Optimizar el Tamaño de Archivos PDF en Ruby
type: docs
weight: 80
url: es/java/optimize-pdf-file-size-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Optimizar el Tamaño de Archivos PDF

Para optimizar el tamaño del archivo de un documento PDF usando **Aspose.PDF Java para Ruby**, llama al método **optimize_filesize** del módulo **Optimize**.

Código Ruby

```java

 def optimize_filesize()

    # La ruta al directorio de documentos.

    data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

    # Abre un documento pdf.

    doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

    # Optimiza el tamaño del archivo eliminando objetos no utilizados

    opt = Rjb::import('aspose.document.OptimizationOptions').new

    opt.setRemoveUnusedObjects(true)

    opt.setRemoveUnusedStreams(true)

    opt.setLinkDuplcateStreams(true)

    doc.optimizeResources(opt)

    # Guarda el documento de salida

    doc.save(data_dir + "Optimized_Filesize.pdf")

    puts "Tamaño de archivo PDF optimizado, por favor verifica el archivo de salida."

end 
```


## Descargar Código en Ejecución

Download **Optimizar el Tamaño del Archivo PDF (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)