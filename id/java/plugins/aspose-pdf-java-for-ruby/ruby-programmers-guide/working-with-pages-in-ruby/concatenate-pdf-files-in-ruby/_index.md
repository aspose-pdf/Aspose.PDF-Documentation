---
title: "Menggabungkan file PDF dalam Ruby"
linktitle: "Menggabungkan file PDF dalam Ruby"
type: docs
weight: 10
url: /id/java/concatenate-pdf-files-in-ruby/
description: Gabungkan beberapa PDF menjadi satu dokumen menggunakan Ruby dan Aspose.PDF secara efisien.
lastmod: "2026-09-30"
---
## Aspose.PDF - menggabungkan file PDF

Untuk menggabungkan file PDF menggunakan **Aspose.PDF Java for Ruby**, cukup panggil modul **ConcatenatePdfFiles**.

Kode Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf1 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Open the source document

pdf2 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input2.pdf')

# Add the pages of the source document to the target document

pdf1.getPages().add(pdf2.getPages())

# Save the concatenated output file (the target document)

pdf1.save(data_dir+ "Concatenate_output.pdf")

puts "New document has been saved, please check the output file"
```

## Mengunduh kode yang dapat dijalankan

Unduh **Concatenate PDF Files (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/concatenatepdffiles.rb)
