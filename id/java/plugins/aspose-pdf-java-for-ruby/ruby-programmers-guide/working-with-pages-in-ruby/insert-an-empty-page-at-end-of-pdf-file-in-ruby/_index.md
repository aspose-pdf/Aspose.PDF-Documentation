---
title: "Menyisipkan halaman kosong di akhir file PDF dengan Ruby"
linktitle: "Menyisipkan halaman kosong di akhir file PDF dengan Ruby"
type: docs
weight: 60
url: /id/java/insert-an-empty-page-at-end-of-pdf-file-in-ruby/
description: Temukan cara menyisipkan halaman kosong di akhir dokumen PDF menggunakan Ruby dengan Aspose.PDF, menambahkan fleksibilitas pada tugas pemrosesan PDF Anda.
lastmod: "2026-09-30"
---
## Aspose.PDF - sisipkan halaman kosong di akhir file PDF

Untuk Menyisipkan Halaman Kosong di akhir dokumen PDF menggunakan **Aspose.PDF Java for Ruby**, cukup panggil modul **InsertEmptyPageAtEndOfFile**.

Kode Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# insert a empty page in a PDF

pdf.getPages().add()

# Save the concatenated output file (the target document)

pdf.save(data_dir+ "output.pdf")

puts "Empty page added successfully!"
```

## Mengunduh kode yang dapat dijalankan

Unduh **Insert an Empty Page at End of PDF File (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypageatendoffile.rb)
