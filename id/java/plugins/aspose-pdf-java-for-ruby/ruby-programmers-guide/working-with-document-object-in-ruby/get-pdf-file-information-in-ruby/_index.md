---
title: Dapatkan Informasi File PDF di Ruby
linktitle: Dapatkan Informasi File PDF di Ruby
type: docs
weight: 50
url: /id/java/get-pdf-file-information-in-ruby/
description: Ekstrak metadata dan detail dari file PDF secara programatik menggunakan Aspose.PDF di Ruby.
lastmod: "2026-09-29"
---
## Aspose.PDF - Dapatkan Informasi File PDF

Untuk Mendapatkan Informasi File dokumen Pdf menggunakan **Aspose.PDF Java for Ruby**, cukup panggil modul **GetPdfFileInfo**.

Kode Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Get document information

doc_info = doc.getInfo()

# Show document information

puts "Author:-" + doc_info.getAuthor().to_s

puts "Creation Date:-" + doc_info.getCreationDate().to_string

puts "Keywords:-" + doc_info.getKeywords().to_s

puts "Modify Date:-" + doc_info.getModDate().to_string

puts "Subject:-" + doc_info.getSubject().to_s

puts "Title:-" + doc_info.getTitle().to_s
```

## Unduh Kode yang Berjalan

Download\u0412\u00A0**Dapatkan Informasi File PDF (Aspose.PDF)**\u0412\u00Adari\u0412\u00Asalah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getpdffileinfo.rb)
