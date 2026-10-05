---
title: "Mengoptimalkan ukuran file PDF dalam Ruby"
linktitle: "Mengoptimalkan ukuran file PDF dalam Ruby"
type: docs
weight: 80
url: /id/java/optimize-pdf-file-size-in-ruby/
description: Pelajari cara mengurangi ukuran file PDF tanpa mengorbankan kualitas menggunakan Aspose.PDF untuk Ruby.
lastmod: "2026-09-30"
---
## Aspose.PDF - optimalkan ukuran file PDF

Untuk mengoptimalkan ukuran file dokumen PDF menggunakan **Aspose.PDF Java for Ruby**, panggil metode **optimize_filesize** dari modul **Optimize**.

Kode Ruby

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

## Mengunduh kode yang dapat dijalankan

Unduh **Optimalkan Ukuran File PDF (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)
