---
title: Mengonversi file SVG ke format PDF dalam Ruby
type: docs
weight: 60
url: id/java/convert-svg-file-to-pdf-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Mengonversi SVG ke PDF

Untuk mengonversi file SVG ke format PDF menggunakan **Aspose.PDF Java untuk Ruby**, cukup panggil modul **SvgToPdf**.

Kode Ruby

```java

# Jalur ke direktori dokumen.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instansiasi objek LoadOption menggunakan opsi muat SVG

options = Rjb::import('com.aspose.pdf.SvgLoadOptions').new

# Buat objek dokumen

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'Example.svg', options)

# Simpan keluaran ke format XLS

pdf.save(data_dir + "SVG.pdf")

puts "Dokumen telah berhasil dikonversi"
```

## Unduh Kode yang Berjalan

Unduh **Convert SVG to PDF (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/svgtopdf.rb)