---
title: Otimizar o tamanho de arquivo PDF em Ruby
linktitle: Otimizar o tamanho de arquivo PDF em Ruby
type: docs
weight: 80
url: /pt/java/optimize-pdf-file-size-in-ruby/
description: Aprenda a reduzir o tamanho de arquivos PDF sem comprometer a qualidade usando Aspose.PDF for Ruby.
lastmod: "2026-10-06"
---
## Aspose.PDF - otimizar o tamanho de arquivo PDF

Para otimizar o tamanho de arquivo de um documento PDF usando **Aspose.PDF Java for Ruby**, chame o método **optimize_filesize** do módulo **Optimize**.

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

## Baixar o exemplo de código

Baixar **Otimizar Tamanho de PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)
