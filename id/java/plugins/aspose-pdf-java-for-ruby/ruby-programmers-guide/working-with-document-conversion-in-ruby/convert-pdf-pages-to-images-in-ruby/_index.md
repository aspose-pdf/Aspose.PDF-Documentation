---
title: "Mengonversi halaman PDF menjadi gambar dalam Ruby"
linktitle: "Mengonversi halaman PDF menjadi gambar dalam Ruby"
type: docs
weight: 20
url: /id/java/convert-pdf-pages-to-images-in-ruby/
description: Ketahui cara mengkonversi halaman PDF menjadi gambar menggunakan Ruby dengan Aspose.PDF, memudahkan pengekstrakan konten visual dari PDF.
lastmod: "2026-09-30"
---
## Aspose.PDF - konversi halaman PDF menjadi gambar

Untuk mengkonversi semua Halaman menjadi Gambar dari dokumen PDF menggunakan **Aspose.PDF Java for Ruby**, cukup panggil modul **ConvertPagesToImages**.

Kode Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

converter = Rjb::import('com.aspose.pdf.facades.PdfConverter').new

converter.bindPdf(data_dir + 'input1.pdf')

converter.doConvert()

suffix = ".jpg"

image_count = 1

image_format_internal = Rjb::import('com.aspose.pdf.ImageFormatInternal')

while converter.hasNextImage()

В В В  converter.getNextImage(data_dir + "image#{image_count}#{suffix}", image_format_internal.getJpeg())

В В В  image_count +=1

end

puts "PDF pages are converted to individual images successfully!"
```

## Mengunduh kode yang dapat dijalankan

Unduh **Convert PDF pages to Images (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/convertpagestoimages.rb)
