---
title: Optimizar el tamaño del archivo PDF en Ruby
linktitle: Optimizar el tamaño del archivo PDF en Ruby
type: docs
weight: 80
url: /es/java/optimize-pdf-file-size-in-ruby/
description: Aprenda a reducir el tamaño de los archivos PDF sin comprometer la calidad usando Aspose.PDF para Ruby.
lastmod: "2026-09-03"
---
## Aspose.PDF - Optimizar el tamaño del archivo PDF

Para optimizar el tamaño del archivo PDF usando **Aspose.PDF Java for Ruby**, llame al método **optimize_filesize** del módulo **Optimize**.

Código Ruby

```java
 def optimize_filesize()

В В В  # The path to the documents directory.

В В В  data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

В В В  # Open a pdf document.

В В В  doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

В В В  # Optimize the file size by removing unused objects

В В В  opt = Rjb::import('aspose.document.OptimizationOptions').new

В В В  opt.setRemoveUnusedObjects(true)

В В В  opt.setRemoveUnusedStreams(true)

В В В  opt.setLinkDuplcateStreams(true)

В В В  doc.optimizeResources(opt)

В В В  # Save output document

В В В  doc.save(data_dir + "Optimized_Filesize.pdf")

В В В  puts "Optimized PDF Filesize, please check output file."

endВ
```

## Descargar código en ejecución

DownloadВ **Optimizar tamaño de archivo PDF (Aspose.PDF)**В desdeВ cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)
