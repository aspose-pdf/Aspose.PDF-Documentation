---
title: Optimalkan Dokumen PDF untuk Web di Ruby
linktitle: Optimalkan Dokumen PDF untuk Web di Ruby
type: docs
weight: 70
url: /id/java/optimize-pdf-document-for-the-web-in-ruby/
description: Percepat PDF untuk pengiriman web yang lebih cepat dan kurangi ukuran file menggunakan Aspose.PDF di Ruby.
lastmod: "2026-09-29"
---
## Aspose.PDF - Optimalkan PDF untuk Web

Untuk mengoptimalkan dokumen PDF untuk web menggunakan **Aspose.PDF Java for Ruby**, cukup panggil metode **optimize_web** dari В  **Optimize** modul.

Kode Ruby

```java

 def optimize_web()

В В В  # The path to the documents directory.

В В В  data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

В В В  # Open a pdf document.

В В В  doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

В В В  # Optimize for web

В В В  doc.optimize()

В В В  #Save output document

В В В  doc.save(data_dir + "Optimized_Web.pdf")

В В В  puts "Optimized PDF for the Web, please check output file."

end
```В 

## Unduh Kode yang Berjalan

UnduhВ **Optimalkan PDF untuk Web (Aspose.PDF)**В dariВ salah satu situs coding sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)
