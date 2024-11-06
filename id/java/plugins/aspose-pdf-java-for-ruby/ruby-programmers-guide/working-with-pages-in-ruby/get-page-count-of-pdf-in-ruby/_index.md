---
title: Dapatkan Jumlah Halaman PDF di Ruby
type: docs
weight: 40
url: id/java/get-page-count-of-pdf-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Dapatkan Jumlah Halaman

Untuk mendapatkan jumlah halaman dokumen Pdf menggunakan **Aspose.PDF Java untuk Ruby**, cukup panggil modul **GetNumberOfPages**.

Kode Ruby

```java
data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Buat dokumen PDF

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

page_count = pdf.getPages().size()

puts "Jumlah Halaman:" + page_count.to_s
```

## Unduh Kode Berjalan

Unduh **Get Page Count (Aspose.PDF)** dari salah satu situs pemrograman sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getnumberofpages.rb)