---
title: Konversi PDF ke Format SVG dalam Ruby
type: docs
weight: 50
url: /id/java/convert-pdf-to-svg-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Konversi PDF ke SVG

Untuk mengonversi PDF ke format SVG menggunakan **Aspose.PDF Java untuk Ruby**, cukup panggil modul **PdfToSvg**.

Kode Ruby

```java

# Jalur ke direktori dokumen.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Buka dokumen target

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# buat objek dari SvgSaveOptions

save_options = Rjb::import('com.aspose.pdf.SvgSaveOptions').new

# jangan kompres gambar SVG ke arsip Zip

save_options.CompressOutputToZipArchive = false

# Simpan output ke format XLS

pdf.save(data_dir + "Output.svg", save_options)

puts "Dokumen telah berhasil dikonversi"
```

## Unduh Kode Berjalan

Unduh **Konversi PDF ke Format SVG (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftosvg.rb)