---
title: Dapatkan Halaman Tertentu dalam File PDF di Ruby
type: docs
weight: 30
url: id/java/get-a-particular-page-in-a-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Dapatkan Halaman

Untuk mendapatkan Halaman Tertentu dalam dokumen PDF menggunakan **Aspose.PDF Java untuk Ruby**, cukup panggil modul **GetPage**.

Kode Ruby

```java
# Jalur ke direktori dokumen.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Buka dokumen target

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# dapatkan halaman di indeks tertentu dari Koleksi Halaman

pdf_page = pdf.getPages().get_Item(1)

# buat objek Dokumen baru

new_document = Rjb::import('com.aspose.pdf.Document').new

# tambahkan halaman ke koleksi halaman dari objek dokumen baru

new_document.getPages().add(pdf_page)

# simpan file PDF yang baru dihasilkan

new_document.save(data_dir + "output.pdf")

puts "Proses selesai dengan sukses!"
```

## Unduh Kode yang Berjalan

Unduh **Dapatkan Halaman (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getpage.rb)