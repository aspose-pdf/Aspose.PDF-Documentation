---
title: Optimizar el tamaño de archivo PDF en Ruby
linktitle: Optimizar el tamaño de archivo PDF en Ruby
type: docs
weight: 80
url: /es/java/optimize-pdf-file-size-in-ruby/
description: Aprenda a reducir el tamaño de archivo de los PDFs sin comprometer la calidad usando Aspose.PDF para Ruby.
lastmod: "2026-09-29"
---
## Aspose.PDF - optimizar el tamaño de archivo PDF

Para optimizar el tamaño de archivo del documento PDF usando **Aspose.PDF Java para Ruby**, llame al método **optimize_filesize** del módulo **Optimize**.

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

Descargar **Optimizar tamaño de PDF (Aspose.PDF)** de cualquier de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)
