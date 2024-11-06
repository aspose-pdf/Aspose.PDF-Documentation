---
title: Menyisipkan Halaman Kosong di Akhir File PDF di Ruby
type: docs
weight: 60
url: id/java/insert-an-empty-page-at-end-of-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Menyisipkan Halaman Kosong di Akhir File PDF

Untuk menyisipkan halaman kosong di akhir dokumen PDF menggunakan **Aspose.PDF Java untuk Ruby**, cukup panggil modul **InsertEmptyPageAtEndOfFile**.

Kode Ruby

```java
# Jalur ke direktori dokumen.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Buka dokumen target

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# sisipkan halaman kosong dalam PDF

pdf.getPages().add()

# Simpan file keluaran yang telah dikonkatenasi (dokumen target)

pdf.save(data_dir+ "output.pdf")

puts "Halaman kosong berhasil ditambahkan!"
```

## Unduh Kode Berjalan

Unduh **Menyisipkan Halaman Kosong di Akhir File PDF (Aspose.PDF)** dari salah satu situs pemrograman sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypageatendoffile.rb)