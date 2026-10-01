---
title: "Mengonversi HTML ke Format PDF di Ruby"
linktitle: "Mengonversi HTML ke Format PDF di Ruby"
type: docs
weight: 10
url: /id/java/convert-html-to-pdf-format-in-ruby/
description: Pelajari cara mengkonversi konten HTML ke format PDF dalam Ruby menggunakan Aspose.PDF untuk pembuatan dokumen yang andal dan akurat.
lastmod: "2026-09-30"
---
## Aspose.PDF - konversi HTML ke Format PDF

Untuk mengkonversi HTML ke format PDF menggunakan **Aspose.PDF Java for Ruby**, cukup panggil modul **HtmlToPdf**.

Kode Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

htmloptions = Rjb::import('com.aspose.pdf.HtmlLoadOptions').new(data_dir)

# Load HTML file

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + "index.html", htmloptions)

# Save the concatenated output file (the target document)

pdf.save(data_dir + "html.pdf")

puts "Document has been converted successfully"
```

## Mengunduh kode yang dapat dijalankan

Unduh **Convert HTML to PDF Format (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/htmltopdf.rb)
