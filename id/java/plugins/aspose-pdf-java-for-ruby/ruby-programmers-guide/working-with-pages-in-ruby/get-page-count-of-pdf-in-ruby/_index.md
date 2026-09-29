---
title: Dapatkan Jumlah Halaman PDF dalam Ruby
linktitle: Dapatkan Jumlah Halaman PDF dalam Ruby
type: docs
weight: 40
url: /id/java/get-page-count-of-pdf-in-ruby/
description: Ambil total jumlah halaman dalam dokumen PDF secara programatis menggunakan Ruby dengan Aspose.PDF.
lastmod: "2026-09-29"
---
## Aspose.PDF - Dapatkan Jumlah Halaman

Untuk mendapatkan jumlah halaman dokumen Pdf menggunakan **Aspose.PDF Java for Ruby**, cukup panggil modul **GetNumberOfPages**.

Kode Ruby

```java
data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Create PDF document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

page_count = pdf.getPages().size()

puts "Page Count:" + page_count.to_s
```

## Unduh Kode yang Berjalan

DownloadВ **Dapatkan Jumlah Halaman (Aspose.PDF)**В dariВ salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getnumberofpages.rb)
