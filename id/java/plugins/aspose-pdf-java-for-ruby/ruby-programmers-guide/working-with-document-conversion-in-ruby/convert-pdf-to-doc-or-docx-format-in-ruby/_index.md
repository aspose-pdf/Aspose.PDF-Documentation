---
title: "Mengonversi PDF ke format DOC atau DOCX di Ruby"
linktitle: "Mengonversi PDF ke format DOC atau DOCX di Ruby"
type: docs
weight: 30
url: /id/java/convert-pdf-to-doc-or-docx-format-in-ruby/
description: Pelajari cara mengonversi dokumen PDF ke format DOC atau DOCX dalam Ruby dengan Aspose.PDF, memungkinkan pengeditan dan pemrosesan yang lebih mudah.
lastmod: "2026-09-30"
---
## Aspose.PDF - konversi PDF ke DOC atau DOCX

Untuk mengonversi dokumen PDF ke format DOC atau DOCX menggunakan **Aspose.PDF Java for Ruby**, cukup panggil modul **PdfToDoc**.

Kode Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Save the concatenated output file (the target document)

pdf.save(data_dir + "output.doc")

puts "Document has been converted successfully"
```

## Mengunduh kode yang dapat dijalankan

Unduh **Convert PDF to DOC atau DOCX (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftodoc.rb)
