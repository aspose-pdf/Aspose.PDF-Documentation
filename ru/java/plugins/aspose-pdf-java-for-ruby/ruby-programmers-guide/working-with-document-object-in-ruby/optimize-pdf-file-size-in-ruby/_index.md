---
title: Оптимизация размера PDF-файла в Ruby
linktitle: Оптимизация размера PDF-файла в Ruby
type: docs
weight: 80
url: /ru/java/optimize-pdf-file-size-in-ruby/
description: Узнайте, как уменьшить размер PDF-файлов без потери качества, используя Aspose.PDF for Ruby.
lastmod: "2026-08-19"
---
## Aspose.PDF - Оптимизация размера PDF-файла

Чтобы оптимизировать размер PDF‑документа с помощью **Aspose.PDF Java for Ruby**, вызовите метод **optimize_filesize** модуля **Optimize**.

Код Ruby

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

## Скачать работающий код

СкачатьВ **Оптимизировать размер PDF (Aspose.PDF)**В сВ любой из нижеупомянутых сайтов для совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)

