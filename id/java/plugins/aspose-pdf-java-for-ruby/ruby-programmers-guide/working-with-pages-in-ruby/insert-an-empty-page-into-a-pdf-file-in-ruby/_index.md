---
title: Sisipkan Halaman Kosong ke dalam File PDF di Ruby
linktitle: Sisipkan Halaman Kosong ke dalam File PDF di Ruby
type: docs
weight: 70
url: /id/java/insert-an-empty-page-into-a-pdf-file-in-ruby/
description: Pelajari cara menyisipkan halaman kosong ke lokasi tertentu dalam dokumen PDF menggunakan Ruby dan Aspose.PDF untuk manajemen dokumen yang presisi.
lastmod: "2026-09-29"
---
## Aspose.PDF - Sisipkan Halaman Kosong

Untuk Menyisipkan Halaman Kosong ke dalam dokumen Pdf menggunakan **Aspose.PDF Java for Ruby**, cukup panggil modul **InsertEmptyPage**.

Kode Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# insert a empty page in a PDF

pdf.getPages().insert(1)

# Save the concatenated output file (the target document)

pdf.save(data_dir+ "output.pdf")

puts "Empty page added successfully!"
```

## Unduh Kode yang Berjalan

UnduhВ **Insert an Empty Page (Aspose.PDF)**В dariВ salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypage.rb)
