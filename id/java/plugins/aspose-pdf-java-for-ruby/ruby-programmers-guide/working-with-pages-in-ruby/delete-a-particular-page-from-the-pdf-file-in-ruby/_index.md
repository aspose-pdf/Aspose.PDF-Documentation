---
title: Hapus Halaman Tertentu dari File PDF di Ruby
type: docs
weight: 20
url: /id/java/delete-a-particular-page-from-the-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Hapus Halaman

Untuk menghapus Halaman Tertentu dari dokumen PDF menggunakan **Aspose.PDF Java untuk Ruby**, cukup panggil modul **DeletePage**.

Kode Ruby

```java
# Jalur ke direktori dokumen.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Buka dokumen target

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# hapus halaman tertentu

pdf.getPages().delete(2)

# simpan file PDF yang baru dihasilkan

pdf.save(data_dir + "output.pdf")

puts "Halaman berhasil dihapus!"
```

## Unduh Kode yang Berjalan

Unduh **Hapus Halaman (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/deletepage.rb)