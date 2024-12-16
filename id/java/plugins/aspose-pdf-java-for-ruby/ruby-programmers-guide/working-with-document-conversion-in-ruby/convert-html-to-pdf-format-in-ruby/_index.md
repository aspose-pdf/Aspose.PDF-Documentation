---
title: Konversi HTML ke Format PDF dalam Ruby
type: docs
weight: 10
url: /id/java/convert-html-to-pdf-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Konversi HTML ke Format PDF

Untuk mengonversi HTML ke format PDF menggunakan **Aspose.PDF Java untuk Ruby**, cukup panggil modul **HtmlToPdf**.

Kode Ruby

```java

# Jalur ke direktori dokumen.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

htmloptions = Rjb::import('com.aspose.pdf.HtmlLoadOptions').new(data_dir)

# Muat file HTML

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + "index.html", htmloptions)

# Simpan file keluaran yang digabungkan (dokumen target)

pdf.save(data_dir + "html.pdf")

puts "Dokumen telah berhasil dikonversi"
```

## Unduh Kode Berjalan

Unduh **Konversi HTML ke Format PDF (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/htmltopdf.rb)