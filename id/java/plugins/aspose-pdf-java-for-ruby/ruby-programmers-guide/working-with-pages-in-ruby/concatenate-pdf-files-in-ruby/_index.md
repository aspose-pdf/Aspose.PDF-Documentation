---
title: Menggabungkan File PDF di Ruby
type: docs
weight: 10
url: id/java/concatenate-pdf-files-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Menggabungkan File PDF

Untuk menggabungkan file PDF menggunakan **Aspose.PDF Java untuk Ruby**, cukup panggil modul **ConcatenatePdfFiles**.

Kode Ruby

```java
# Jalur ke direktori dokumen.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Buka dokumen target

pdf1 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Buka dokumen sumber

pdf2 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input2.pdf')

# Tambahkan halaman dari dokumen sumber ke dokumen target

pdf1.getPages().add(pdf2.getPages())

# Simpan file keluaran yang telah digabungkan (dokumen target)

pdf1.save(data_dir+ "Concatenate_output.pdf")

puts "Dokumen baru telah disimpan, silakan periksa file keluaran"
```

## Unduh Kode Berjalan

Unduh **Menggabungkan File PDF (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/concatenatepdffiles.rb)