---
title: Mengonversi Halaman PDF ke Gambar dalam Ruby
type: docs
weight: 20
url: /java/convert-pdf-pages-to-images-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Mengonversi Halaman PDF ke Gambar

Untuk mengonversi semua Halaman menjadi Gambar dari dokumen Pdf menggunakan **Aspose.PDF Java untuk Ruby**, cukup panggil modul **ConvertPagesToImages**.

Kode Ruby

```java

# Jalur ke direktori dokumen.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

converter = Rjb::import('com.aspose.pdf.facades.PdfConverter').new

converter.bindPdf(data_dir + 'input1.pdf')

converter.doConvert()

suffix = ".jpg"

image_count = 1

image_format_internal = Rjb::import('com.aspose.pdf.ImageFormatInternal')

while converter.hasNextImage()

    converter.getNextImage(data_dir + "image#{image_count}#{suffix}", image_format_internal.getJpeg())

    image_count +=1

end

puts "Halaman PDF berhasil dikonversi menjadi gambar individual!"
```

## Unduh Kode Berjalan

Unduh **Convert PDF pages to Images (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/convertpagestoimages.rb)