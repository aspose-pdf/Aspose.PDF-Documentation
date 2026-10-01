---
title: "Mengatur informasi file PDF di Ruby"
linktitle: "Mengatur informasi file PDF di Ruby"
type: docs
weight: 120
url: /id/java/set-pdf-file-information-in-ruby/
description: Secara terprogram mendefinisikan dan memperbarui metadata PDF seperti judul, penulis, dan kata kunci menggunakan Ruby.
lastmod: "2026-09-30"
---
## Aspose.PDF - atur informasi file PDF

Untuk memperbarui informasi dokumen Pdf menggunakan **Aspose.PDF Java for Ruby**, cukup panggil modul **SetPdfFileInfo**.

Kode Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Get document information

doc_info = doc.getInfo()

doc_info.setAuthor("Aspose.PDF for java")

doc_info.setCreationDate(Rjb::import('java.util.Date').new)

doc_info.setKeywords("Aspose.PDF, DOM, API")

doc_info.setModDate(Rjb::import('java.util.Date').new)

doc_info.setSubject("PDF Information")

doc_info.setTitle("Setting PDF Document Information")

# save update document with new information

doc.save(data_dir + "Updated_Information.pdf")

puts "Update document information, please check output file."
```

## Mengunduh kode yang dapat dijalankan

Download **Set PDF File Information (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setpdffileinfo.rb)
