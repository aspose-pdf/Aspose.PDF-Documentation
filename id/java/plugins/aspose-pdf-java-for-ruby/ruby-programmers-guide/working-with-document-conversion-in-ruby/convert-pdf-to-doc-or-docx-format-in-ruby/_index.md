---
title: Konversi PDF ke format DOC atau DOCX dalam Ruby
type: docs
weight: 30
url: id/java/convert-pdf-to-doc-or-docx-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Konversi PDF ke DOC atau DOCX

Untuk mengonversi dokumen PDF ke format DOC atau DOCX menggunakan **Aspose.PDF Java for Ruby**, cukup panggil modul **PdfToDoc**.

Kode Ruby

```java

# Jalur ke direktori dokumen.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Buka dokumen target

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Simpan file keluaran yang dikonkat (dokumen target)

pdf.save(data_dir + "output.doc")

puts "Dokumen telah berhasil dikonversi"
```

## Unduh Kode Berjalan

Unduh **Konversi PDF ke DOC atau DOCX (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftodoc.rb)