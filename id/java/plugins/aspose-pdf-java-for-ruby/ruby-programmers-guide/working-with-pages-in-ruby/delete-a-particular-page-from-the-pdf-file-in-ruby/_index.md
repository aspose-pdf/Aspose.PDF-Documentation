---
title: "Menghapus halaman tertentu dari file PDF di Ruby"
linktitle: "Menghapus halaman tertentu dari file PDF di Ruby"
type: docs
weight: 20
url: /id/java/delete-a-particular-page-from-the-pdf-file-in-ruby/
description: Hapus halaman tertentu dari file PDF secara terprogram menggunakan Aspose.PDF for Ruby.
lastmod: "2026-09-30"
---
## Aspose.PDF - hapus halaman

Untuk menghapus Halaman Tertentu dari dokumen PDF menggunakan **Aspose.PDF Java for Ruby**, cukup panggil modul **DeletePage**.

Kode Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# delete a particular page

pdf.getPages().delete(2)

# save the newly generated PDF file

pdf.save(data_dir + "output.pdf")

puts "Page deleted successfully!"
```

## Mengunduh kode yang dapat dijalankan

Unduh **Delete Page (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/deletepage.rb)
